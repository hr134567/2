from daum_news_fnc import get_news_title_and_content
import requests
from bs4 import BeautifulSoup

# 다음 뉴스 웹사이트 페이지(15건)를 돌면서 기사(제목+본문) 수집
page = 3
count = 0
for page_num in range(1, page+1) :
    print(f"****************************** {page_num}page *********************************")
    url = f"https://news.daum.net/breakingnews/digital?page={page_num}"

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    title_list = soup.select("ul.list_news2 a.link_txt")

    for i, tag in enumerate(title_list) :
        count += 1
        new_url = tag["href"]
        title, content = get_news_title_and_content(new_url)
        print(f"URL = {new_url}")
        print(f"{count} 뉴스제목 : {title}")
        print(f"{count} 뉴스본문 : {content}")