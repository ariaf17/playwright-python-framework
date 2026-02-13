import json
from pathlib import Path


def load_test_data(file_name: str):
    data_path = Path(__file__).parent.parent / "data" / file_name
    with open(data_path, "r") as f:
        return json.load(f)