import requests
from bs4 import BeautifulSoup as bs
import datetime
import sqlite3
from src import display
def update_series():
    conn = sqlite3.connect("./movies.db")
    c = conn.cursor()
    today_date = datetime.datetime.today()

    c.execute("SELECT ID,Name,Season FROM series")
    fetch = c.fetchall()
    for i,name,sea in fetch:
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
                print(ep_list.a.text,air_date.date(),i)
                c.execute("""UPDATE series SET Last_ep = ?,Aired_on = ? WHERE Name = ?""",[str(ep_list.a.text),str(air_date.date()),name])
                conn.commit()
                break
    display.display_series()
    c.close()
    conn.close()
    
if __name__ =="__main__":
    update_series()