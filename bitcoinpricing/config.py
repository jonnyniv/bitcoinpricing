from typing import List

import yaml
from jsonschema import validate
from jsonschema.exceptions import ValidationError

schema = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'url': {'type': 'string'},
            'decode': {'type': 'array', 'items': {'type': 'string'}},
            'params': {'type': 'object'}
        },
        'required': ['name', 'url', 'decode']
    }
}


def load_site_config(filename: str, config_schema: dict) -> List[dict]:
    with open(filename, 'r') as f:
        config = yaml.load(f)
    try:
        validate(config, config_schema)
    except ValidationError:
        raise
    else:
        return config


if __name__ == '__main__':
    with open('sites.yml', 'r') as f:
        validate(yaml.load(f), schema)
