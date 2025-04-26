import os
import json
import urllib.parse
import urllib.request

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API keys from environment variables
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# Base URLs
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


def get_json(url: str) -> dict:
    """
    Get JSON response
    """
    try:
        print(f"[DEBUG] Fetching URL: {url}")  # Debug print
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode('utf-8')
            return json.loads(response_text)
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
        print(f"URL: {url}")
        return {}
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return {}


def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Get latitude and longitude from place name
    """
    place_name_encoded = urllib.parse.quote(place_name)
    url = f"{MAPBOX_BASE_URL}/{place_name_encoded}.json?access_token={MAPBOX_TOKEN}"

    data = get_json(url)

    try:
        coordinates = data["features"][0]["geometry"]["coordinates"]
        longitude, latitude = coordinates #Mapbox returns (longitude, latitude)
        print(f"[DEBUG] Latitude: {latitude}, Longitude: {longitude}")  # Debug print
        return (str(latitude), str(longitude))
    except (IndexError, KeyError):
        print("[DEBUG] Could not find coordinates for the place.")
        return (None, None)


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Get station_name, wheelchair_accessible from latitude and longitude
    """
    url = (
        f"{MBTA_BASE_URL}?api_key={MBTA_API_KEY}"
        f"&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance"
    )

    print(f"[DEBUG] MBTA API URL: {url}")  # Debug print

    data = get_json(url)

    try:
        stop_info = data["data"][0]
        stop_name = stop_info["attributes"]["name"]
        wheelchair_code = stop_info["attributes"]["wheelchair_boarding"]

        #Wheelchair codes: 1 (accessible), 2 (not accessible), 0 (unknown)
        is_wheelchair_accessible = wheelchair_code == 1

        print(f"[DEBUG] Nearest Station: {stop_name}, Wheelchair Accessible: {is_wheelchair_accessible}")  # Debug
        return (stop_name, is_wheelchair_accessible)
    except (IndexError, KeyError):
        print("[DEBUG] Could not find a nearby station.")
        return (None, None)


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Get nearest MBTA stop and wheelchair accessibility from place name
    """
    latitude, longitude = get_lat_lng(place_name)
    if latitude is None or longitude is None:
        return (None, None)
    return get_nearest_station(latitude, longitude)


def main():
    """
    """
    place = input("Enter a place name or address")
    stop_name, accessible = find_stop_near(place)

    if stop_name:
        print(f"The nearest MBTA stop is '{stop_name}'.")
        print(f"Wheelchair Accessible: {'Yes' if accessible else 'No'}")
    else:
        print("No station found near that location.")


if __name__ == "__main__":
    main()
