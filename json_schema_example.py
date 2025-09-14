from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 5},
        "age": {"type": "number"},
    },
    "required": ["name"]
}

data = {
    "name": "Ann",
    "age": 40,
}

validate(instance=data, schema=schema)