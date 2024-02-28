# learn about Object Oriented Programming by answering these questions

# 1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model.
# Then create an instance of this class.

# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full
# name of the car (brand and model).

# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the
# Car class and has an additional attribute battery_size.

# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute,
# making it private, and provide a getter method for it.

# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type
# in both Car and ElectricCar classes, but with different behaviors.

# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the
# number of cars created.

# 7. Static Method
# Problem: Add a static method to the Car class that returns
# a general description of a car.

# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make
# the model attribute read-only.

# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check 
# if my_tesla is an instance of Car and ElectricCar.

# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the
# ElectricCar class inherit from both, demonstrating multiple
# inheritance.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charhe"


myCar = Car("tata", "toyota")
# print(myCar.brand)
# print(myCar.model)
# print(myCar.fullname())
# print(myCar.get_brand())
# print(myCar.fuel_type())
# print(myCar.general_description())

myElectricCar = ElectricCar("tesla", "Model s", "85kWh")
# print(myElectricCar.fuel_type())
# print(myElectricCar.general_description())
print(myElectricCar.model)

print(Car.total_car)
print(Car.general_description())

print(isinstance(myElectricCar, ElectricCar))
print(isinstance(myElectricCar, Car))


class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass