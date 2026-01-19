# Source: Row 487 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx


def make_homeserver(self, reactor, clock):
    hs = self.setup_test_homeserver(
        "server", http_client=None, federation_sender=Mock()
    )
    return hs