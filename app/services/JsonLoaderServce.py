from pathlib import Path
import json

def get_data(name : str):
    BASE_PATH = Path(__file__).resolve().parent.parent
    file_path = f"{BASE_PATH}/utils/sample_data/{name}.json"

    with open(file_path, "r" , encoding="utf-8") as file:
        data = json.load(file)

    return data