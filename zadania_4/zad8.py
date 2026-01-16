import requests
import argparse

class Brewery:
    def __init__(self, name: str, brewery_type: str, city: str):
        self.name = name
        self.brewery_type = brewery_type
        self.city = city

    def __str__(self):
        return f"Brewery: {self.name} | Type: {self.brewery_type} | City: {self.city}"

parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str)
args = parser.parse_args()

if args.city:
    url = f"https://api.openbrewerydb.org/v1/breweries?by_city={args.city}&per_page=20"
else:
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

response = requests.get(url)

data = response.json()
breweries = []
for item in data:
    brewery = Brewery(
        name=item["name"],
        brewery_type=item["brewery_type"],
        city=item["city"]
    )
    breweries.append(brewery)

for x in breweries:
    print(x)