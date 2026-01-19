# Source: Row 6 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_787.xlsx

def testEditDistanceBadIndices(self):
    hypothesis_indices = np.full((3, 3), -1250999896764, dtype=np.int64)
    hypothesis_values = np.empty(3, dtype=np.int64)
    hypothesis_shape = np.empty(3, dtype=np.int64)
    truth_indices = np.full((3, 3), -1250999896764, dtype=np.int64)
    truth_values = np.full([3], 2, dtype=np.int64)
    truth_shape = np.full([3], 2, dtype=np.int64)
    expected_output = []  # dummy; ignored

    self._testEditDistance(
    hypothesis=(hypothesis_indices, hypothesis_values, hypothesis_shape),
    truth=(truth_indices, truth_values, truth_shape),
    normalize=False,
    expected_output=expected_output,
    expected_err_re=(r"inner product -\d+ which would require writing "
                        "to outside of the buffer for the output tensor")
    )