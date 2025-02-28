import mysql.connector

class Database :
    def __init__(self):
        self.conn= mysql.connector.connect(
            host ="localhost",
            user ="felopater",
            password ="Felo6262#",
            database="pythondb"
        )
        self.cursor = self.conn.cursor(dictionary=True)  

        print(type(self.cursor))

    def select (self ,sql,params=None):
        self.cursor.execute(sql ,params or())
        return self.cursor.fetchall()
    def update (self , sql ,params=None):
        self.cursor.execute(sql,params or ())
        self.conn.commit()
    def close(self):
        self.cursor.close()
        self.conn.close()



db=Database()