from nturl2path import url2pathname
import site
from urllib import response
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
st.title('NEWS SITE SCRAPING')
url = 'https://scroll.in/editorspick'
# getting data from internet
response = requests.get(url)
# response.status_code
# 200
data = response.text
# parsing the data
soup = BeautifulSoup(data)
cards = soup.find('div', {'class' : 'row-stories column scroll-box scroll-box-3'})
for card in cards.find_all('div', {'class' : 'row-story-meta'}):
    if 'adBg' not in card.attrs.get('class'):
        print(card.find('h1').text)
        print(card.find('h2').text)
        print(card.find('h5').text)
        news = []

for card in cards.find_all('div', {'class' : 'row-story-meta'}):
    if 'adBg' not in card.attrs.get('class'):
        newsDetail = {}
        newsDetail['headlineabout'] = (card.find('h1').text)
        newsDetail['description'] = (card.find('h2').text)
        newsDetail['dataPublished'] = (card.find('h5').text)
        news.append(newsDetail)
for detail in news:
    c1, c2 = st.columns((1, 3))
    c1.markdown(f"""<img src="{detail.get('image')}" style="width: 100%" />""", unsafe_allow_html=True)
    c2.subheader(detail.get('headlineabout'))
    c2.markdown(detail.get('description'))
    c2.text(detail.get('dataPublished'))

df = pd.DataFrame(news)
df.to_csv('news_data.csv')
df.to_html('news_data.html')
