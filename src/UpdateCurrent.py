import requests
from bs4 import BeautifulSoup as bs
import datetime
import pandas as pd

def update_series():
    df = pd.read_csv("../csv/Choice.csv")
    df.drop_duplicates(inplace = True)
    today_date = datetime.datetime.today()

    for index,row in df.iterrows():
        zeroes = "0"*(7-int(len(str(row["ID"]))))
        base_url = "https://www.imdb.com/title/tt"+zeroes+str(row["ID"])+"/episodes?season="+str(row["Season"])+"&ref_=tt_eps_sn_"+str(row["Season"])
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
                df.loc[index,"Last_ep"] = ep_list.a.text
                df.loc[index,"Aired on"] = air_date.date()
                break
    df = df.iloc[:,1:]            
    df.to_csv("../csv/Current.csv")
    print(df)

if __name__ =="__main__":
    update_series()