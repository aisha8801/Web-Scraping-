from nturl2path import url2pathname
import site
from urllib import response
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
st.title('NEWS SITE SCRAPING')
url = 'https://www.ndtv.com/top-stories'
# getting data from internet
response = requests.get(url)
# response.status_code
# 200
data = response.text
# parsing the data
soup = BeautifulSoup(data)
cards = soup.find('div', {'class' : 'lisingNews'})
for card in cards.find_all('div', {'class' : 'news_Itm'}):
    if 'adBg' not in card.attrs.get('class'):
        print(card.find('h2').text)
        print(card.find('span').text)
        print(card.find('p').text)
        news = []

for card in cards.find_all('div', {'class' : 'news_Itm'}):
    if 'adBg' not in card.attrs.get('class'):
        newsDetail = {}
        newsDetail['title'] = (card.find('h2').text)
        newsDetail['author'] = (card.find('span').text)
        newsDetail['summary'] = (card.find('p').text)
        news.append(newsDetail)
for detail in news:
    c1, c2 = st.columns((1, 3))
    c1.markdown(f"""<img src="{detail.get('image')}" style="width: 100%" />""", unsafe_allow_html=True)
    c2.subheader(detail.get('title'))
    c2.text(detail.get('author'))
    c2.markdown(detail.get('Summary'))

df = pd.DataFrame(news)
df.to_csv('news_data.csv')
df.to_html('news_data.html')

