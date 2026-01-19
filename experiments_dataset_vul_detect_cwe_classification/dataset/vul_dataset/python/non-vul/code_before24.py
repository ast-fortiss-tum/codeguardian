# Source: Row 539 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def setUp(self):
    self.reactor = ThreadedMemoryReactorClock()
    self.hs_clock = Clock(self.reactor)
    self.homeserver = setup_test_homeserver(
        self.addCleanup,
        federation_http_client=None,
        clock=self.hs_clock,
        reactor=self.reactor,
    )