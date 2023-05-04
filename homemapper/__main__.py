import requests as re
import os
import json

BING_API_KEY = os.environ['BING_API_KEY']
url = f"https://dev.virtualearth.net/REST/v1/Routes/Isochrones?key={BING_API_KEY}"

res = re.post(
    url,
    json={
        "waypoint": "51.512819550956415,-0.09056628289369296",
        "maxTime": 15,
        "travelMode": "transit",
        "distanceUnit": "mi"
    }
)

print(res.json())