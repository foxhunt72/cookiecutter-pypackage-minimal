"""Load config."""

import os
import sys
import yaml

from .__version__ import __project_name__


def config_read(config=""):
    """Load config from disk.

    Args:
        config: config path to load.

    Returns:
        config
    """
    if config is None or config == "":
        config = f"~/.{__project_name__}.yaml"

    try:
        with open(os.path.expanduser(config), "r") as file:
            config_dict = yaml.load(file, Loader=yaml.FullLoader)
    except Exception as e:  # noqa:B902
        sys.stderr.write(f"can't open config file: {config}  {e}\n")
        print("please create it....")
        sys.exit(1)
    return config_dict

