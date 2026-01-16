import requests

class Brewery:
    def __init__(self, name: str, brewery_type: str):
        self.name = name
        self.brewery_type = brewery_type

    def __str__(self):
        return f"Brewery: {self.name} | Type: {self.brewery_type}"

response = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=20")

data = response.json()
breweries = []
for item in data:
    brewery = Brewery(
        name=item["name"],
        brewery_type=item["brewery_type"]
    )
    breweries.append(brewery)

for x in breweries:
    print(x)