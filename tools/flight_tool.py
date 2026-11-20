import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "flights.json"

def search_flights(source, destination):
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        flights = json.load(file)

    results = [
        flight for flight in flights
        if source.lower() in str(flight).lower()
        and destination.lower() in str(flight).lower()
    ]

    return results