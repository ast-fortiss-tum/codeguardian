# Source: Row 8 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_94.xlsx

def load(self, stream):
    '''read vault steam and return python object'''
    return yaml.safe_load(self.vault.decrypt(stream))