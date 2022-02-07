import json
from pprint import pprint
import requests

def get_data() -> dict:
    url = "https://api.alternative.me/fng/?limit=0"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        raise Exception(f"fear and greed API responded with a {res.status_code} status code")

def get_series() -> list:
    data = get_data()
    series = [get_element(x) for x in data["data"]]
    return series

def get_element(raw_element: dict) -> dict:
    return {
        "value": raw_element["value"],
        "timestamp": raw_element["timestamp"]
    }

if __name__ == "__main__":
    series = get_series()
    pprint(series)