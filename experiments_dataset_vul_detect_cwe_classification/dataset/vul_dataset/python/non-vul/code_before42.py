# Source: Row 369 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

def parse_yaml_query(yaml_content):
    """Parses the given YAML string to attempt to extract a query.

    Args:
        yaml_content: A string containing YAML content.

    Returns:
        On success, the processed MLQuery object.
    """
    logger.debug("Attempting to parse YAML content:\n%s" % yaml_content)
    return parse_query(yaml.safe_load(yaml_content))