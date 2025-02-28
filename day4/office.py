from Database import Database

class Office:
    
    def __init__(self,name,employees,db):
        self.name=name
        self.employees=employees
        self.db=db
        self.cursor = self.db.cursor

    def get_all_employee(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()
    
    def get_employee(self,id):
        return self.db.query("select * from employee where id =%s",(id,))
   
    def fire(self,id):
        self.cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
        self.db.conn.commit()
        print(f"Employee {id} has been fired.")

    
    def hire(self,name,email,workH,distanceToWork,salary):
        self.cursor.execute("INSERT INTO employees (name, email, workH, distanceToWork, salary) VALUES (%s, %s, %s, %s, %s)", 
                            (name, email, workH, distanceToWork, salary))
        self.db.conn.commit()
        print(f"{name} has been hired.")

    def deduct(self,empid,deduct):
        self.cursor.execute("UPDATE employees SET salary = salary - %s WHERE id = %s", (deduct, empid))
        self.db.conn.commit()
    #    print(f"deduct from employee  {empid} = {deduct} your salary is {empid.salary}",empid,deduct,empid.salary)
    
    def reward(self,empid,reward):
        self.cursor.execute("UPDATE employees SET salary = salary + %s WHERE id = %s", (reward, empid))
        self.db.conn.commit()
        #print("reward  employee  %s = $s your salary is %s",empid,reward,empid.salary)
    
    def calculate_lateness(self,empid,moveHour):
        if moveHour < 9:
            self.reward(empid,10)
            print("youu are in time")

        else :
           self.deduct(empid,10)    
           print("youu are late")
       
  
db = Database()
office = Office("TechCorp", 50, db)
#office.hire("Omar", "omar@yah.com", 8, 5, 5000)
# office.hire("felopater", "felo@yahoo.com", 8, 5, 5000)
# office.hire("mom", "mo@yah.com", 8, 5, 8000)
# office.hire("fady", "fady@yahoo.com", 5, 5, 6000)
# office.hire("hamdy", "hamdy@yahoo.com", 8, 5, 4000)

employees = office.get_all_employee()
for emp in employees:
    print(emp)
office.deduct(11, 200)
office.reward(10, 300)
office.calculate_lateness(13, 10)   
office.fire(5) 
