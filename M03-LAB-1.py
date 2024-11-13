#By Kyle Clemons

#Creates superclass for vehicles
class Vehicle:
    def __init__(self):
        pass
class automobile(Vehicle):
    def __init__(self,year,make,model,doors,roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#Asks for attributes for the Vehicle sub-class, test code
#automobile1 = automobile("2024", "Dodge", "Hellcat", "4", "Solid")

year = int(input("What is the model year of your car? "))
make = input("What is the make of your car? ")
model = input("What is the model of your car? ")
doors = int(input("How many doors are on your car? "))
roof = input("Is your car a solid-top or a convertible? ")

#Extra error correction code. Unused.
#Checks for a valid vehicle year.
#if year != int:
#   print("Please type a number for the vehicle's model year")
#    input("What is the make of your car? ")

#if year <= 1900:
#   print("Please type a number for the vehicle's model year")
#1    input("What is the model year of your car?  ")

#Checks for valid roof and door types.
#if roof != "solid" or "sun roof" or "sun-roof" or "solid-top":
#    print("Invalid roof type.")
#    input("Do you have a solid roof or sun-roof? ")

#if doors != "2" or "4":
#    print("Invalid door types.")
#    input("How many doors do you have? ")

#Will print out the input for the Vehicle subclass
print(automobile,year,make,model,doors,roof)

#Individual inputs for each Vehicle subclass input
#automobile2 = int(input(automobile.year()))
#automobile2 = input(automobile.make())
#automobile2 = input(automobile.model())
#automobile2 = input(automobile.doors())
#automobile2 = input(automobile.roof())

#print(automobile2.year)
#print(automobile2.make)
#print(automobile2.model)
#print(automobile2.doors)
#print(automobile2.roof)