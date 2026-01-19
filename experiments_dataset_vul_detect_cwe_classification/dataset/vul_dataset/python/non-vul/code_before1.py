# Source: Row 764 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def test_double_linefeed(self):
        self.assertEqual(self._callFUT(b"\n\n"), 2)