# Source: Row 17 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_78.xlsx

def scriptPath(*pathSegs):
    startPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(startPath, *pathSegs)
    return path

