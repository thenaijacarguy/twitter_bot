import tweepy
import requests
from bs4 import BeautifulSoup
# keys and tokens
bearer_token = 'xxxxxx'
consumer_key = 'xxxxxx'
consumer_secret = 'xxxxxxxx'
access_token = 'xxxxxxx'
access_secret = 'xxxxxxxxx'

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_token=access_token, access_token_secret=access_secret)
# assigning the article url to a variable
article_url = 'https://www.theverge.com/tech'

# getting the html with the requests library
response = requests.get(article_url)

# creating a beautiful soup object with the text gotten from the response of the request
soup = BeautifulSoup(response.text, 'html.parser')

# fetching the title of the first article
article = soup.find('a', class_='after:absolute')
title = article.find_next('a').text

# the body
body = soup.find_all('p')[1].text

# the link to the article
link = article.find_next('a')['href']

# the variable containing the content of the tweet
tweet = '#DailyTechNews: ' + title + ' - ' + body[:150] + '...Read More Here 👇🏼 https://theverge.com' + link

client.create_tweet(text=tweet)
