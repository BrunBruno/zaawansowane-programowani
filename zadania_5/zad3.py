class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int) -> None:
        Property.__init__(self, area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House: {self.area} m^2, {self.rooms} r, {self.price} $, {self.address}, {self.plot} m^2"

class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int) -> None:
        Property.__init__(self, area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat: {self.area} m^2, {self.rooms} r, {self.price} $, {self.address}, {self.floor} f"


house = House(
    area=150,
    rooms=5,
    price=2_000_000,
    address="Katowice",
    plot=1800
)

flat = Flat(
    area=80,
    rooms=3,
    price=500_000,
    address="Chorzów",
    floor=2
)

print(house)
print(flat)