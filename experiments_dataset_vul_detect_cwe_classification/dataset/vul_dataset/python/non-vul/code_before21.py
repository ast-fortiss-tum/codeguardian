# Source: Row 15 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_502.xlsx

def to_yaml(self, **kwargs):
    """Returns a yaml string containing the network configuration.

    To load a network from a yaml save file, use
    `keras.models.model_from_yaml(yaml_string, custom_objects={})`.

    `custom_objects` should be a dictionary mapping
    the names of custom losses / layers / etc to the corresponding
    functions / classes.

    Args:
        **kwargs: Additional keyword arguments
            to be passed to `yaml.dump()`.

    Returns:
        A YAML string.

    Raises:
        ImportError: if yaml module is not found.
    """
    if yaml is None:
      raise ImportError(
          'Requires yaml module installed (`pip install pyyaml`).')
    return yaml.dump(self._updated_config(), **kwargs)