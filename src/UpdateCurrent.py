import requests
from bs4 import BeautifulSoup as bs
import datetime
import pandas as pd
import sqlite3
import display

def update_series():
    conn = sqlite3.connect("./movies.db")
    c = conn.cursor()
  #  df = pd.read_csv("./csv/Choice.csv")
  #  df.drop_duplicates(inplace = True)
    today_date = datetime.datetime.today()

    c.execute("SELECT ID,Name,Season FROM series")
    
   # for index,row in df.iterrows():
    for i,name,sea in c.fetchall():
        zeroes = "0"*(7-int(len(str(i))))
        base_url = "https://www.imdb.com/title/tt"+zeroes+str(i)+"/episodes?season="+str(sea)+"&ref_=tt_eps_sn_"+str(sea)
        r = requests.get(base_url,verify =False)
        page_html = r.text
        page_soup = bs(page_html,"html.parser")
        r.close()
        ep_list_container = page_soup.find_all("div",class_ = "info")

        for i in range(len(ep_list_container)-1,-1,-1):
            ep_list =ep_list_container[i]
            if ep_list.div.text.strip()=="":
                continue
            if "." in  ep_list.div.text.strip():  
                air_date = datetime.datetime.strptime(ep_list.div.text.strip(), '%d %b. %Y')
            else:
                air_date = datetime.datetime.strptime(ep_list.div.text.strip(), '%d %b %Y')
            if air_date <= today_date:
                c.execute("""UPDATE series SET Last_ep =(?),Aired_on =(?) WHERE ID = (?)""",[ep_list.a.text,air_date.date(),i])
           #     df.loc[index,"Last_ep"] = ep_list.a.text
          #      df.loc[index,"Aired on"] = air_date.date()
                break
    #df = df.iloc[:,1:]            
   # df.to_csv("./csv/Current.csv")
    display.display_series()
    c.close()
    conn.close()
    
if __name__ =="__main__":
    update_series()