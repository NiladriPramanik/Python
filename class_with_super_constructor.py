class Vehicle:
    def __init__(self , mileage , cost ):
        self.mileage=mileage
        self.cost=cost
    
    def show_vehicle_details(self):
        print("I am a vehicle")
        print("Mileage of vehicle is ",self.mileage)
        print("Cost of vehicle is ",self.cost)

v1=Vehicle(35,800000)

class Car(Vehicle):

    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp

    def show_car_details(self):

        print("I am a car")
        print("Mileage of car is ",self.mileage)
        print("Cost of car is ",self.cost)
        print("Number of tyres is ",self.tyres)
        print("Horse Power is ",self.hp) 

c1=Car(20,300000,4,800)

#invoking methods

c1.show_vehicle_details()



    
    
        
