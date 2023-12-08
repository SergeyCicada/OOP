class House:
    def __init__(self, number, color, owner):
        self.number = number
        self.color = color
        self.owner = owner

    def get_owner(self):
        return self.owner


house_1 = House(10, "red", "John")
house_2 = House(11, "green", "Micle")
house_3 = House(12, "white", "Alvares")

print(house_1.owner)
print(house_2.owner)
print(house_3.owner)

owner_name = house_1.get_owner()
print(owner_name)
