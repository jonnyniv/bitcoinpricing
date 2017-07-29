import yaml
import jsonschema


schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "url": {"type": "string"},
            "decode": {"type": "array", "items": {"type": "string"}},
            "params": {"type": "object"}
        },
        "required": ["name", "url", "decode"]
    }
}


if __name__ == '__main__':
    with open("sites.yml", 'r') as f:
        jsonschema.validate(yaml.load(f), schema)