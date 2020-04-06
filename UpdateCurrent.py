from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import datetime
import pandas as pd

def update_series():
    df = pd.read_csv("./csv/Choice.csv")
    df.drop_duplicates(inplace = True)
    today_date = datetime.datetime.today()

    for i in df.index:
        base_url = "https://www.imdb.com/title/tt"+df["ID"][i]+"/episodes?season="+str(df["Season"][i])+"&ref_=tt_eps_sn_"+str(df["Season"][i])
        
        uClient = urlopen(base_url)
        page_html = uClient.read()
        uClient.close()
        page_soup = bs(page_html,"html.parser")
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
                df["Last_ep"][i] = ep_list.a.text
                df["Aired on"][i] = air_date.date()])
                break

    df.to_csv("./csv/Choice.csv",header=False)
    print(df)

if __name__ =="__main__":
    update_series()