import imdb

def add_series():
    ia = imdb.IMDb()
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
                details.append(mov.movieID)
                details.append(tv.get('title'))
                season = input("Enter Season Number:")
                details.append(season)
                break
            elif choice == "next":
                continue
            else:
                break
        loop = input("Add more?(y/n):").lower()
        if loop =="n":
            print(details)
            break    

if __name__ == "__main__":
    add_series()        