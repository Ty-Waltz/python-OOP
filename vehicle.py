class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
        def update_owner(self, new_owner):
              self.owner = new_owner


        def __str__(self):
            return(f"Registration number:{self.registration_number}\n"
            f"Type: {self.type}\n"
            f"Owner: {self.owner}")


vehicle_one = Vehicle(2355674, "SUV", "Ryan")
vehicle_two = Vehicle(7583926, "Sadan", "Susan")


print("Original status:")
print(vehicle_one)
print(vehicle_two)


vehicle_one.update_owner("Greg")
vehicle_two.update_owner("Bob")


print("Updated status:")
print(vehicle_one)
print(vehicle_two)
