import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "hotels.json"

def search_hotels(city):
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        hotels = json.load(file)

    return [
        hotel for hotel in hotels
        if city.lower() in str(hotel).lower()
    ]