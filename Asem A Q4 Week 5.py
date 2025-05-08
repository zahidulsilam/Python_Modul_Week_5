class Vehicle :
    def __init__(self,Brand_of_vehicle,Vehicle_model,Year_of_manufacture_of_the_vehicle):
        self.make = Brand_of_vehicle
        self.model = Vehicle_model
        self.year = Year_of_manufacture_of_the_vehicle
        

class SUV (Vehicle):
    def __init__(self, Brand_of_vehicle, Vehicle_model, Year_of_manufacture_of_the_vehicle,four_wheel_drive):
        super().__init__(Brand_of_vehicle, Vehicle_model, Year_of_manufacture_of_the_vehicle)
        self.suv = four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self, Brand_of_vehicle, Vehicle_model, Year_of_manufacture_of_the_vehicle,max_speed):
        super().__init__(Brand_of_vehicle, Vehicle_model, Year_of_manufacture_of_the_vehicle)
        self.max_speed = max_speed

suv = SUV('Ford','Explorar' , 2022, True)

print(f'Off road vehicle (SUV):\nBrand of vehicle:{suv.make}\nVehicle model:{suv.model}\nYear of the manfactur:{suv.year}')

Sports_Car = SportsCar('Porshe','Cabrio',2025,330)
print (f'Sports Car:\nBrand of vehicle:{Sports_Car.make}\nVehicle model:{Sports_Car.model}\nYear of the manfactur:{Sports_Car.year}\nMax speed:{Sports_Car.max_speed}')