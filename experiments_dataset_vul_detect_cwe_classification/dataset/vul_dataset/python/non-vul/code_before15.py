# Source: Row 661 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def test_str(self):
        code = LoginCode(user=self.user, timestamp=datetime(2018, 7, 1))
        self.assertEqual(str(code), 'test_user - 2018-07-01 00:00:00')
