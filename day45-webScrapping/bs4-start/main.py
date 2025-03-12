from bs4 import BeautifulSoup

# Introduction 
# with open('portfolio.html') as file:
#     contents = file.read()  
#     # print(contents)

# # open with BeautifulSoup   
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.name)
# # print(soup.title.string) # or text

# # print(soup.prettify())

# # print(soup.get('href'))

# find_all_h2 = soup.find_all('h2')
# # print(find_all_h2)

# # for h2 in find_all_h2:
# #     # print(h2.getText())
# #     print(h2.text)

# find_ = soup.find_all(name='h2')
# # print(find_)

# # Using selectors  
# # name = soup.select_one(selector="section h2")
# name = soup.select(selector="section h2")
# # print(name)

# scrapping live website 
import requests

url = "https://news.ycombinator.com/"
res = requests.get(url)
# print(res.text)

yc_web_page = res.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.title)

""" Get the first title ... """
# news_title_span = soup.find(name='span', class_='titleline')

# article_tag = news_title_span.find('a')
# # article_link = article_tag['href']
# article_link = article_tag.get('href')

# article_upvote = soup.find(name='span', class_='score').getText()

# # print(news_title_span)
# print(article_tag.text)
# print(article_link)
# print(article_upvote)


""" Get all the titles """
news_title_span = soup.find_all(name='span', class_='titleline')

article_tags = []
article_links = []
for article_tag in news_title_span:
    tag = article_tag.find('a')
    if tag:
        article_tags.append(tag.text)  # gets the <a 
        article_links.append(tag.get('href')) # gets the href
    
article_upvotes = [int(score.getText().split(' ')[0]) for score in soup.find_all(name='span', class_='score')]  # list comprehension


# print(article_tags)
# print(article_links)
# print(article_upvotes)

# Print out the title and link for the story with the highest number of upvotes
largest_number = max(article_upvotes)
l_index = (article_upvotes.index(largest_number))

# print(len(article_upvotes))
print(article_tags[l_index])
print(article_links[l_index])




