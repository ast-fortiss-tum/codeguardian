# Source: Row 608 in ./dataset/CVEfixes/Analysis/results/Python/df_python_all.xlsx

  def to_yaml(self, **kwargs):
    """Returns a yaml string containing the network configuration.

    Note: Since TF 2.6, this method is no longer supported and will raise a
    RuntimeError.

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
        RuntimeError: announces that the method poses a security risk
    """
    raise RuntimeError(
        'Method `model.to_yaml()` has been removed due to security risk of '
        'arbitrary code execution. Please use `model.to_json()` instead.'
    )