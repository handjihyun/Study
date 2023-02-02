def daegu(path):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen(path)
    bs = BeautifulSoup(html.read(), 'html.parser')

    print(f"현재 위치: {bs.select_one('h2.title').text}")
    print(f"현재 온도: {bs.select_one('div.temperature_text > strong').text}")
    print(f"날씨 상태: {bs.select_one('span.weather').text}")
    print(f"공기 상태:")
    for i in range(1, 5):
        print(bs.select_one('ul.today_chart_list').text.split('   ')[i].strip())
    print(f'{"-"*25}\n{"시간대별 날씨 및 온도"}\n{"-"*25}')
    #for i in range(0, len(bs.select_one('div.graph_inner').text.split('       '))):
        #print(bs.select_one('div.graph_inner').text.split('       ')[i].strip())
    weather_time = bs.find_all('li', {'class':'_li'})
    for i in weather_time:
        print(i.text.strip())

path = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8'
daegu(path)