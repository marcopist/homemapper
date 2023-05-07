import requests as re
from homemapper.constants import NOMINATIM_API_URL
import json

def find_branches(name, city):
    """This function uses the Open Street Map Nominatim API
        to find the branches of a chain shop in a given city.
    
    Args:
        name (str): The name of the chain store.
        city (str): The name of the city.
        
    Returns:
        list: A list of coordinates of the branches. Up to 60 branches are returned.
    """
    endpoint = NOMINATIM_API_URL + "/search"

    response = re.get(
        endpoint,
        params={
            "q": name + " " + city,
            "limit": 50,
            "format": "jsonv2",
        }
    )
    # Open street map is being extra nice and returns a JSON array, not a JSON object. (:
    results = json.loads('{ "data" :' + response.text + '}')['data']

    return results