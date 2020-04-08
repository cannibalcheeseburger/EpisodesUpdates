import pandas as pd
from texttable import Texttable
import display
import os

def mod_del():
    df = pd.read_csv("../csv/Choice.csv",index_col=[0])
    while(True):
        display.display_series()
        print(df)
        table = Texttable()
        table.header(["Name","Season"])
        Entry = int(input("Enter the entry no. you want to modify/delete:"))
        if(Entry<len(df)):
            print("Entry Selected:\n")
            table.add_row([df.iloc[[Entry]]["Name"],df.iloc[[Entry]]["Season"]])
            print(table.draw())
            ch = input("1. Delete Entry\n2. Change Entry Season\nEnter Input:")
            if(ch=='1'):
                df = df.drop(df.index[Entry])
                input("Enter to proceed...")
            elif(ch =='2'):
                df.loc[Entry,"Season"] = input("\nEnter Season Number:")
                print(df)
                input("Enter to proceed...")
            else:
                input("Invalid Response!!")
            os.system("clear")           

        else:
            print("Invalid")    

if __name__ == "__main__":
    mod_del()      