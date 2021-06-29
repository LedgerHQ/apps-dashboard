#!/usr/bin/env python3

"""
Validate every yaml files against apps.schema.
"""

import glob
import jsonschema
import os
import yaml


def yaml_load(path):
    with open(path) as fp:
        data = fp.read()
    return yaml.load(data, Loader=yaml.SafeLoader)


def validate_yaml(path, validator):
    """
    Raises jsonschema.exceptions.ValidationError if the yaml file is invalid.
    """
    document = yaml_load(path)
    validator.validate(document)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))

    schema_file = os.path.join(script_dir, "apps.schema")
    schema = yaml_load(schema_file)
    validator = jsonschema.Draft7Validator(schema)

    apps_dir = os.path.join(script_dir, "..", "apps")
    files = glob.glob(f"{apps_dir}/*.yaml")
    for path in files:
        validate_yaml(path, validator)
