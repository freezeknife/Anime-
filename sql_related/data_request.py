# Using API to create a MyAnime List Database
# Documentation: https://mal-api.readthedocs.io/en/latest/
from mal import Anime
import sqlite3
import time
# establish database connection
con = sqlite3.connect("Anime_database.db")
# establish database cursor
cur = con.cursor()
#create a table if it exists
cur.execute("CREATE TABLE IF NOT EXISTS My_Anime_List(id INT PRIMARY KEY,title_english VARCHAR(1000), genres TEXT, rating FLOAT, studios TEXT, score FLOAT, episodes INTEGER, related_anime TEXT, url TEXT)")
i = 13554
counter = 0
count_entry = 0
while True:
    try:
        time.sleep(2)
        count_entry += 1
        if count_entry == 50:
            count_entry = 0 # The API has a rate limit
            time.sleep(300) 
        anime = Anime(i)
        title_english =    anime.title_english      
        genres= anime.genres  
        genres = str(genres)      
        rating=      anime.rating   
        studios =   anime.studios
        studios =   str(studios)
        score =      anime.score 
        episodes =  anime.episodes    
        related_anime = anime.related_anime
        related_anime = str(related_anime)
        url =      anime.url       
        print(i ,title_english, genres, rating, studios, score, episodes, related_anime, url)
        cur.execute("INSERT INTO My_Anime_List VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (i ,title_english, genres, rating, studios, score, episodes, related_anime, url))
        anime.reload()
        con.commit()
        i += 1
    except:
        i = i + 1
        counter += 1
        print(counter)
        if counter == 100000: # Should not exceed the counter, if exceed we will find a workaround
            break
   
