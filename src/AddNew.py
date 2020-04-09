import imdb
import sqlite3

def add_series():
    conn = sqlite3.connect("./movies.db")
    c = conn.cursor()
    ia = imdb.IMDb()
    while(True):
        movie = input("Enter name of Series:")
        movie_obj =  ia.search_movie(movie)
        for mov in movie_obj:
            tv = ia.get_movie(mov.movieID)
            print(tv.get('title'))
            print(tv.get('plot')[0])
            choice = input("Is this it?(Y/N/next)").lower()
            if choice == "y":
                season = input("Enter Season Number:")
                c.execute("INSERT INTO series(ID,Name,Season) VALUES ((?),(?),(?))",[mov.movieID,tv.get('title'),season])
                conn.commit()
                break
            elif choice == "next":
                continue
            else:
                break
        loop = input("Add more?(y/n):").lower()
        if loop =="n":
            c.execute("SELECT ID,Name,Season FROM series")
            for tup in c.fetchall():
                print(tup)
            break    
    c.close()
    conn.close()    


if __name__ == "__main__":
    add_series()        