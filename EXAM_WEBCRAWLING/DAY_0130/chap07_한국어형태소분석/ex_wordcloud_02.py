# -------------------------------------
# 네이버 뉴스 타이틀 Word Cloud
# -------------------------------------

from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import re
import platform

def get_titles(start_num, end_num, search_word, title_list):
    while 1:
        if start_num > end_num:
            break
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'.format(search_word, start_num)
        req = requests.get(url)
        time.sleep(1)

        if req.ok:
            soup = BeautifulSoup(req.text, 'html.parser')
            list_news = soup.find('ul', class_ = 'list_news')
            li_bxs = list_news.find_all('li', class_ = 'bx')

            for li_bx in li_bxs:
                news_title = li_bx.find('a', class_ = 'news_tit')
                title_list.append(news_title['title'])
        start_num += 10
    print(title_list)

def make_wordcloud(word_count, title_list):
    okt = Okt()

    sentences_tag = []

    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-' * 30)

    print(sentences_tag)
    print('\n' * 3)

    noun_adj_list = []

    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)
    
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    print(tags)

    if platform.system() == 'Windows':
        path = r'c:\Windows\Fonts\malgun.ttf'
    else:
        path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    wc = WordCloud(font_path=path, background_color='white', width=800, height=600)
    print(dict(tags))
    cloud = wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

if __name__ == '__main__':
    search_word = '빅데이터'
    title_list = []
    get_titles(1, 20, search_word, title_list)
    make_wordcloud(20, title_list)