// Source: Row 3 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_918.xlsx

handler: function ({command} = {}) {
    const [, protocol, ip, port] = _.chain(command).get('arg', '').split('|').value();
    const family = FAMILY[protocol];
    if (!family) return this.reply(504, 'Unknown network protocol');

    this.connector = new ActiveConnector(this);
    return this.connector.setupConnection(ip, port, family)
    .then(() => this.reply(200));
  },