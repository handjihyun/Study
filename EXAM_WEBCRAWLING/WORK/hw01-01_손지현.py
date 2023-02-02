def scraping_use_find(path):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen(path)
    bs = BeautifulSoup(html.read(), 'html.parser')

    print("National Weather Service Scraping")
    print("-"*35)
    print("[find 함수 사용]")
    print(f"총 tombstone-container 검색 개수: {len(bs.find('div', {'id':'seven-day-forecast-container'}).find_all('div', class_ = 'tombstone-container'))}")
    print("-"*80)

    for i in range(9):
        print(f"[Period]: {bs.find_all('p', class_ = 'period-name')[i].text}")
        print(f"[Short desc]: {bs.find_all('p', class_ = 'short-desc')[i].text}")
        print(f"[Temperature]: {bs.find_all('p', class_ = 'temp')[i].text}")
        print(f"[Image desc]: {bs.find_all('div', class_ = 'col-sm-2 forecast-label')[i].text}: {bs.find_all('div', class_ = 'col-sm-10 forecast-text')[i].text}")
        print("-"*80)

# -------------------------------------------------------------------------------------
def scraping_use_select(path):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    html = urlopen(path)
    bs = BeautifulSoup(html.read(), 'html.parser')
    # bs = BeautifulSoup(html, 'html.parser')

    print("National Weather Service Scraping")
    print("-"*35)
    print("[select 함수 사용]")
    print(f"총 tombstone-container 검색 개수: {len(bs.select('div.tombstone-container'))}")
    print("-"*80)

    for i in range(9):
        print(f"[Period]: {bs.select('p.period-name')[i].text}")
        print(f"[Short desc]: {bs.select('p.short-desc')[i].text}")
        print(f"[Temperature]: {bs.select('p.temp')[i].text}")
        print(f"[Image desc]: {bs.select('div.col-sm-2')[i].text}: {bs.select('div.col-sm-10')[i].text}")
        print("-"*80)


path1 = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y9DTi3ZBz18'
scraping_use_find(path1)
scraping_use_select(path1)