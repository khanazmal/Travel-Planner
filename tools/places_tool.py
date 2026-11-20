import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "places.json"

def search_places(city):
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        places = json.load(file)

    return [
        place for place in places
        if city.lower() in str(place).lower()
    ]