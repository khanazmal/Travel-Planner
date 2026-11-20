import os
from dotenv import load_dotenv
from google import genai

from tools.flight_tool import search_flights
from tools.hotel_tool import search_hotels
from tools.places_tool import search_places

load_dotenv(override=True)

def plan_trip(city, source):
    flights = search_flights(source, city)
    hotels = search_hotels(city)
    places = search_places(city)

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    You are an AI Travel Planner.

    Plan a practical trip from {source} to {city}.

    Available flights:
    {flights}

    Available hotels:
    {hotels}

    Places to visit:
    {places}

    Create:
    1. Day-wise travel itinerary
    2. Suggested sightseeing order
    3. Food suggestions
    4. Travel tips

    Use the provided flight, hotel and places data.
    Clearly mention if data is unavailable.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return {
        "flights": flights,
        "hotels": hotels,
        "places": places,
        "itinerary": response.text
    }


