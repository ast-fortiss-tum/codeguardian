# Source: Row 123 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_20.xlsx

def post(self):
    """This method handles the POST requests to add agents to the Cloud Verifier.

    Currently, only agents resources are available for POSTing, i.e. /agents. All other POST uri's will return errors.
    agents requests require a json block sent in the body
    """
    session = get_session()
    try:
        rest_params = web_util.get_restful_params(self.request.uri)
        if rest_params is None:
            web_util.echo_json_response(
                self, 405, "Not Implemented: Use /agents/ interface")
            return

        if not web_util.validate_api_version(self, rest_params["api_version"], logger):
            return

        if "agents" not in rest_params:
            web_util.echo_json_response(self, 400, "uri not supported")
            logger.warning('POST returning 400 response. uri not supported: %s', self.request.path)
            return

        agent_id = rest_params["agents"]

        if agent_id is not None:
            # If the agent ID is not valid (wrong set of
            # characters), just do nothing.
            if not validators.valid_agent_id(agent_id):
                web_util.echo_json_response(self, 400, "agent_id not not valid")
                logger.error("POST received an invalid agent ID: %s", agent_id)
                return

            content_length = len(self.request.body)
            if content_length == 0:
                web_util.echo_json_response(
                    self, 400, "Expected non zero content length")
                logger.warning('POST returning 400 response. Expected non zero content length.')
            else:
                json_body = json.loads(self.request.body)
                agent_data = {}
                agent_data['v'] = json_body['v']
                agent_data['ip'] = json_body['cloudagent_ip']
                agent_data['port'] = int(json_body['cloudagent_port'])
                agent_data['operational_state'] = states.START
                agent_data['public_key'] = ""
                agent_data['tpm_policy'] = json_body['tpm_policy']
                agent_data['meta_data'] = json_body['metadata']
                agent_data['allowlist'] = json_body['allowlist']
                agent_data['mb_refstate'] = json_body['mb_refstate']
                agent_data['ima_sign_verification_keys'] = json_body['ima_sign_verification_keys']
                agent_data['revocation_key'] = json_body['revocation_key']
                agent_data['accept_tpm_hash_algs'] = json_body['accept_tpm_hash_algs']
                agent_data['accept_tpm_encryption_algs'] = json_body['accept_tpm_encryption_algs']
                agent_data['accept_tpm_signing_algs'] = json_body['accept_tpm_signing_algs']
                agent_data['supported_version'] = json_body['supported_version']
                agent_data['ak_tpm'] = json_body['ak_tpm']
                agent_data['mtls_cert'] = json_body.get('mtls_cert', None)
                agent_data['hash_alg'] = ""
                agent_data['enc_alg'] = ""
                agent_data['sign_alg'] = ""
                agent_data['agent_id'] = agent_id
                agent_data['boottime'] = 0
                agent_data['ima_pcrs'] = []
                agent_data['pcr10'] = None
                agent_data['next_ima_ml_entry'] = 0
                agent_data['learned_ima_keyrings'] = {}
                agent_data['verifier_id'] = config.get('cloud_verifier', 'cloudverifier_id', fallback=cloud_verifier_common.DEFAULT_VERIFIER_ID)
                agent_data['verifier_ip'] = config.get('cloud_verifier', 'cloudverifier_ip')
                agent_data['verifier_port'] = config.get('cloud_verifier', 'cloudverifier_port')

                # TODO: Always error for v1.0 version after initial upgrade
                if agent_data['mtls_cert'] is None and agent_data['supported_version'] != "1.0":
                    web_util.echo_json_response(self, 400, "mTLS certificate for agent is required!")
                    return

                is_valid, err_msg = cloud_verifier_common.validate_agent_data(agent_data)
                if not is_valid:
                    web_util.echo_json_response(self, 400, err_msg)
                    logger.warning(err_msg)
                    return

                try:
                    new_agent_count = session.query(
                        VerfierMain).filter_by(agent_id=agent_id).count()
                except SQLAlchemyError as e:
                    logger.error('SQLAlchemy Error: %s', e)
                    raise e

                # don't allow overwriting

                if new_agent_count > 0:
                    web_util.echo_json_response(
                        self, 409, f"Agent of uuid {agent_id} already exists")
                    logger.warning("Agent of uuid %s already exists", agent_id)
                else:
                    try:
                        # Add the agent and data
                        session.add(VerfierMain(**agent_data))
                        session.commit()
                    except SQLAlchemyError as e:
                        logger.error('SQLAlchemy Error: %s', e)
                        raise e

                    # add default fields that are ephemeral
                    for key,val in exclude_db.items():
                        agent_data[key] = val

                    # Prepare SSLContext for mTLS connections
                    agent_mtls_cert_enabled = config.getboolean('cloud_verifier', 'agent_mtls_cert_enabled', fallback=False)
                    mtls_cert = agent_data['mtls_cert']
                    agent_data['ssl_context'] = None
                    if agent_mtls_cert_enabled and mtls_cert:
                        agent_data['ssl_context'] = web_util.generate_agent_mtls_context(mtls_cert, self.mtls_options)

                    if agent_data['ssl_context'] is None:
                        logger.warning('Connecting to agent without mTLS: %s', agent_id)

                    asyncio.ensure_future(
                        process_agent(agent_data, states.GET_QUOTE))
                    web_util.echo_json_response(self, 200, "Success")
                    logger.info('POST returning 200 response for adding agent id: %s', agent_id)
        else:
            web_util.echo_json_response(self, 400, "uri not supported")
            logger.warning("POST returning 400 response. uri not supported")
    except Exception as e:
        web_util.echo_json_response(self, 400, f"Exception error: {str(e)}")
        logger.warning("POST returning 400 response. Exception error: %s", e)
        logger.exception(e)