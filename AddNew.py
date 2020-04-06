import imdb
import pandas as pd


def add_series():
    header = ["ID","Name","Season","Last_ep","Aired on"]
    ia = imdb.IMDb()
    df = pd.DataFrame(columns=header)
    while(True):
        movie = input("Enter name of Series:")
        details = []
        movie_obj =  ia.search_movie(movie)
        for mov in movie_obj:
            tv = ia.get_movie(mov.movieID)
            print(tv.get('title'))
            print(tv.get('plot')[0])
            choice = input("Is this it?(Y/N/next)").lower()
            if choice == "y":
                season = input("Enter Season Number:")
                df = df.append(pd.Series([mov.movieID,tv.get('title'),season],index = header[:3]),ignore_index=True)
                break
            elif choice == "next":
                continue
            else:
                break
        loop = input("Add more?(y/n):").lower()
        if loop =="n":
            df.to_csv('./csv/Choice.csv', mode='a', header=False)
            print(df)
            break    


if __name__ == "__main__":
    add_series()        