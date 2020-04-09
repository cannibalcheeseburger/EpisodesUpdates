import sqlite3
from texttable import Texttable
import os
from src import display

def mod_del():
    conn = sqlite3.connect("./movies.db")
    c = conn.cursor()
    #df = pd.read_csv("./csv/Choice.csv",index_col=[0])
    while(True):
        display.display_series()
        table = Texttable()
        table.header(["ID","Name","Season"])
        Entry = input("Enter the ENTRY ID you want to modify/delete:")
        #if Entry in f:
        c.execute("SELECT Name,Season FROM series WHERE ID = ?",(Entry,))
        name,sea = c.fetchone()
        print("Entry Selected:\n")
        table.add_row([Entry,name,sea])
        print(table.draw())
        ch = input("1. Delete Entry\n2. Change Entry Season\nEnter Input:")
        if(ch=='1'):
            c.execute("DELETE FROM series WHERE ID = ?",(Entry,))
            conn.commit()
            #df = df.drop(df.index[Entry])
            input("Enter to proceed...")
        elif(ch =='2'):
            sno = input("\nEnter Season Number:")
            c.execute("UPDATE series SET Season = ? WHERE ID = ? ",[sno,Entry])
            conn.commit()
            display.display_series()
            input("Enter to proceed...")
        else:
            input("Invalid Response!!")
        os.system("clear")           

        #else:
        #    print("Invalid")   
        #    input("Enter Anything...")
       #     os.system("clear") 

if __name__ == "__main__":
    mod_del()      