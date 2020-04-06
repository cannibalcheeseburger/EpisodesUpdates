from bs4 import BeautifulSoup as bs
from urllib.request import urlopen 
import datetime

today_date = datetime.datetime.today()
urls = {"Brooklyn Nine-Nine":"https://www.imdb.com/title/tt2467372/episodes?season=7&ref_=tt_eps_sn_7",
        "The Walking Dead":"https://www.imdb.com/title/tt1520211/episodes?season=10&ref_=tt_eps_sn_10",
        "Westworld":"https://www.imdb.com/title/tt0475784/episodes?season=3&ref_=tt_eps_sn_3"}

for url in urls.keys():
    uClient = urlopen(urls[url])
    page_html = uClient.read()
    uClient.close()
    index_short =0
    page_soup = bs(page_html,"html.parser")
    ep_list_container = page_soup.find_all("div",class_ = "info")

    for i in range(len(ep_list_container)-1,0,-1):
        ep_list =ep_list_container[i]
        if ep_list.div.text.strip()=="":
            continue
        if "." in  ep_list.div.text.strip():  
            air_date = datetime.datetime.strptime(ep_list.div.text.strip(), '%d %b. %Y')
        else:
            air_date = datetime.datetime.strptime(ep_list.div.text.strip(), '%d %b %Y')
        if air_date <= today_date:
            print(url+": "+ep_list.a.text+"\tAired at:",air_date.date())
            break

