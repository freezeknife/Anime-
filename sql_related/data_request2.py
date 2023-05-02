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
cur.execute("CREATE TABLE IF NOT EXISTS My_Anime_List_2(id INT PRIMARY KEY, title VARCHAR(100),img_url TEXT")
i = 1
counter = 0
count_entry = 0
while True:
    try:
        anime = Anime(i)
        title =    anime.title     
        image_url= anime.image_url
        themes = anime.themes
        themes = str(themes)
        premiered = anime.premiered
        print(i ,title, image_url, themes, premiered)
        cur.execute("INSERT INTO My_Anime_List_2 VALUES (?, ?, ?, ?)", (i ,title, image_url, themes, premiered))
        anime.reload()
        con.commit()
        i += 1
        count_entry += 1
        if count_entry == 20:
            count_entry = 0 # The API has a rate limit
            time.sleep(300) 
    except:
        i = i + 1
        counter += 1
        print(counter)
        if counter == 100000: # Should not exceed the counter, if exceed we will find a workaround
            break