
class Car:
    

    def __init__(self,name,fuelRete,velocity):
        self.name=name
        self.fuelRete=fuelRete
        self.velocity=velocity
    
    def run(self,velocity, distance):
        self.velocity = velocity 
        fuelConsumption_per_km = 0.2  
        totalFuelNeeded = distance * fuelConsumption_per_km

        if self.fuelRate >= totalFuelNeeded:
            self.fuelRate -= totalFuelNeeded

            print(f"The car {self.name} is running at {self.velocity} km/h for {distance} km.")
            print(f"Remaining fuel: {self.fuelRate}L")
        else:
            max_distance = self.fuelRate / fuelConsumption_per_km 

            print(f"Warning! Not enough fuel to reach {distance} km.")
            print(f"The car {self.name} can only run for {max_distance:.2f} km before stopping.")
            self.stop()

    def stop(self):
        self.velocity=0
        print(f"The car {self.name} has stopped due to no fuel or reaching destination.")
