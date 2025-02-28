from person import Person 
from car import car


class Employee(Person):
   

    def __init__(self,id,name,email,workH,distanceToWork,salary=1000):
        super().__init__(self.name, self.money,self.numOfMeal, self.sleepH)  

        self.id=id
        self.name=name
        self.email=email
        self.__salary=salary
        self.workH=workH
        self.distanceToWork=distanceToWork

    def work(self):
        if self.workH ==8 :
            self.mood="Happy"
        if self.workH <8 :
            self.mood="Lazy"
        if self.workH >8 :
            self.mood="Tired"
        print(self.mood)
   
    def drive(self,car,distance):
     
        fuel_consumed = (distance / car.velocity) * 5  
        if car.fuelRate >= fuel_consumed:
            car.fuelRate -= fuel_consumed
            print(f"Car drove {distance} km at {car.velocity} km/h. Fuel remaining: {car.fuelRate}L")
        else:
            print("Not enough fuel to drive!")

   
    def refuel(self,car,gasAmount = 100):
        car.fuelRete +=gasAmount
        print(f"car")

    def send_mail(to, subject, msg, receiver_name):
        pass


