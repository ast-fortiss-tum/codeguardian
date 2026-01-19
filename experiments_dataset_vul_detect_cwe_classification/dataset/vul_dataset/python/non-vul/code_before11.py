# Source: Row 248 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def valid_id(opts, id_):
    '''
    Returns if the passed id is valid
    '''
    try:
        return bool(clean_path(opts['pki_dir'], id_)) and clean_id(id_)
    except (AttributeError, KeyError, TypeError) as e:
        return False