import json

def read_json_safely(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    
    except FileNotFoundError:
        return {}
    
    except json.JSONDecodeError:
        return None