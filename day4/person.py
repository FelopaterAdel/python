

class Person:

    def __init__(self,name,money,numOfMeal,sleepH):
        self.name=name
        self.money=money
        self.mood=("Happy","Lazy","Tired")
        self.sleepH= sleepH
        self.numOfMeal=numOfMeal
        self.healthRate = None

    def sleep(self):
        if self.sleepH ==7 :
            print(self.mood[0])
        if self.sleepH >7 :
            print(self.mood[1])
        if self.sleepH <7 :
            print(self.mood[2])
   
    def eat(self):
        if self.numOfMeal ==3 :
             self.healthReat="100%"
        if  self.numOfMeal ==2 :
             self.healthReat="75%"
        if self.numOfMeal ==1:
             self.healthReat="50%"
        print(self.healthReat)
   
   
    def buy(self,numOfItem):
        self.money -=numOfItem*10
        print(self.money)

person1 = Person("Ahmed", 500, 3, 7)
person1.sleep()  
person1.eat()    
person1.buy(1)   