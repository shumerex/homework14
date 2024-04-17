class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building1 = Building(5, "office")
building2 = Building(10, "residential")

print(building1 == building2)

building3 = Building(5, "office")
print(building1 == building3) 