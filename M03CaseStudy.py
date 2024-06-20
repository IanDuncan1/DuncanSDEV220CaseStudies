class Vehicle:
    type = ""
class Automobile(Vehicle):
    year = 0
    make = ""
    model = ""
    doors = 0
    roof = ""
Automobile.type = input("What type of vehicle? ")
Automobile.year = input("What year? ")
Automobile.make = input("What make? ")
Automobile.model = input("What model? ")
Automobile.doors = input("How many doors? ")
Automobile.roof = input("What type of roof? ")

print('\nVehicle type: ',Automobile.type)
print('Year: ',Automobile.year)
print('Make: ',Automobile.make)
print('Model: ',Automobile.model)
print('Number of doors: ',Automobile.doors)
print('Type of roof: ',Automobile.roof)