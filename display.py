import datetime
from texttable import Texttable
import pandas as pd

def display_series():   
    df =pd.read_csv("./csv/Current.csv",index_col=[0])
    today_date = datetime.datetime.today()
    table = Texttable()
    table.header(["Name","Ep_name","Season","Aired on"])
    for index,row in df.iterrows():
        table.add_row([row["Name"],row["Last_ep"],row["Season"],row["Aired on"]])    
    print(table.draw())        

if __name__ =="__main__":
    display_series()    