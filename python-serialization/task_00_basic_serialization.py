import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a dictionary."""
    with open(filename, 'r') as file:
        return json.load(file)
