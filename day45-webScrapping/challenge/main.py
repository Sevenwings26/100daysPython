# The Best Movies On Netflix UK Right Now — 51 Films You Must Watch In 2025
import requests
from bs4 import BeautifulSoup

# url = "https://www.empireonline.com/movies/features/best-netflix-movies-uk/" 
url = "https://www.empireonline.com/movies/features/best-movies-2/" 

response = requests.get(url)
# print(response) # returns 200
movies_page = response.text

soup = BeautifulSoup(movies_page, 'html.parser')
# print(soup)

# find all element tag h2 
movie_element = soup.find_all('h2')
# print(len(movie_element))

movie_titles = []
# loop through and find strong 
for movie_title in movie_element:
    strong_tag = movie_title.find('strong')
    if strong_tag:
        movie_titles.append(strong_tag.text)


movie_titles.reverse()
# print(movie_titles)

# for index, title in enumerate(movie_titles, start=1):
#     print(f"{index}. {title}")

# for title in movie_titles:
#     print(title)


# Write to a text file 
with open('movies.txt', mode='w') as file:
    for title in movie_titles:
        file.write(f"{title}\n")
