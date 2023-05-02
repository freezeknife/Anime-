# Anime-
## Project Description
Anime is a form of entertainment that has gained widespread popularity in current time where the number of fans has grown to millions and among all age groupincluding myself.
This project aims to create an application which will recommend applications based creating a network of anime titles and recommend new titles based on entered
prefernces or recommend anime titles based on titles a user enjoyed have enjoyed in the past. The data used for the project will be obtained from MAL.

This project will also have a small mini-portion to conduct exploratory analysis on the top 200 anime, we will try to see if there are any common story patterns in the dataset.

## Obtaining Data for the project(in sql_files folder).
Data will be obtained for the project using a MAL API( can be found from https://mal-api.readthedocs.io/en/latest/ ). The data obtained using the API will be stored into an SQL database and 
will be properly cleaned before it can be used in the project for the backend portion of the project. The database i choose to use is SQLite and 
we can use the sqlite3 python library to automate the whole process.

## Backend:
### Recommendation based on user opreferences: 

Based on use preferences, we will create a network of anime titles and identify the closest title based on the similarity of the title. This will basically be a neighboring anime title 
with the msot number of relationships.


### Recommendation based on users wathced anime:

User can enter a set of anime, we will the extract all the data attributed to it like Genre, theme, target age group, etc. Based on that we will implement a page rank algorithm to identify the most 
important anime in that network and if the rating is too low we shall move to the next anime in the page rank.

## Frontend
Have not thought about the final process yet, but currently plan to use flutter for this part.


