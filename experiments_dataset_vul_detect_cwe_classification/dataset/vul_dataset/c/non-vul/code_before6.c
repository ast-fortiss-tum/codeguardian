// Source: Row 6 in ./dataset/CVEfixes/Analysis/results/C/df_c_cwe_79.xlsx

/* restore the OP session_state from the session */
const char *session_state = oidc_session_get_session_state(r, session);
if (session_state == NULL) {
    oidc_warn(r,
            "no session_state found in the session; the OP does probably not support session management!?");
    return DONE;
}