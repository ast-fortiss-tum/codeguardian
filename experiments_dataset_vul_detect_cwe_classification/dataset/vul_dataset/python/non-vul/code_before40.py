# Source: Row 290 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def extension_element_from_string(xml_string):
    element_tree = defusedxml.ElementTree.fromstring(xml_string)
    return _extension_element_from_element_tree(element_tree)