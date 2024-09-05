import json

def serialize_to_json(data):
    return json.dumps(data)

def deserialize_from_json(json_data):
    return json.loads(json_data)
