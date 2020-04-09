from texttable import Texttable
import pandas as pd
import sqlite3

def display_series():
    conn = sqlite3.connect("./movies.db")
    c = conn.cursor()   
    table = Texttable()
    table.header(["ID","Name","Season","Last_ep","Aired on"])
    c.execute("SELECT * FROM series")
    for tup in c.fetchall():
        table.add_row(tup)    
    print(table.draw())    
    c.close()
    conn.close()    

if __name__ =="__main__":
    display_series()    