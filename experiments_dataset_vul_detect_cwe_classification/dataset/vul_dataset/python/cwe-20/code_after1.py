# Source: Row 77 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_20.xlsx

def _handle_carbon_received(self, msg):
    if msg['from'].bare == self.xmpp.boundjid.bare:
        self.xmpp.event('carbon_received', msg)