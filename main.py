import datetime
from texttable import Texttable
import os
import sqlite3
from src import AddNew,display,UpdateCurrent,Mod_del

def create_db():
    conn = sqlite3.connect("./movies.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS series (ID INTEGER PRIMARY KEY ,Name TEXT,Season INTEGER,Last_ep TEXT,Aired_on TEXT)")
    conn.commit()
    c.close()
    conn.close()

def main():
    while(True):
        choose = int(input("1.Add Series\n2.Display Cached Series List \n3.Update List\n4.Modify\Delete an Entry from List\n0.Quit\nEnter your choice(0-4): "))
        os.system("clear")
        if choose == 1:
            AddNew.add_series()
            input("Press anything to proceed:")
        elif choose == 2:
            display.display_series()
            input("Press anything to proceed:")
        elif choose == 3:
            UpdateCurrent.update_series()
            input("Press anything to proceed:")
        elif choose == 4:
            Mod_del.mod_del()
            input("Press Anything to proceed:")
        elif choose == 0:
            return 
        else:
            input("Invalid choice\nPress anything to proceed:")
        os.system('clear')

if __name__ == "__main__":
    create_db()
    main()   