import sqlite3
def init_db():
   a=sqlite3.connect("dayplanner.db")
   cursor=a.cursor()
   cursor.execute("""CREATE TABLE IF NOT EXISTS userdetails(username TEXT NOT NULL,password TEXT NOT NULL)""")
   return a

if __name__=="__main__":
   init_db()