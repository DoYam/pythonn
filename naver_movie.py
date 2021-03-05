import requests
from bs4 import BeautifulSoup
import pandas

def get_movie_point(start, end=1):
    results = []
    for i in range(start, end+1):
        url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'.format(i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")
        trs = bs.select("table.list_netizen > tbody > tr")
        for tr in trs:  #다수의 평점
            # 번호
            number = tr.select_one("td.ac.num").text
            # 작성자
            writer = tr.select_one("td.num > a.author").text
            
            # td 의 title 클래스를 구합니다.
            tr_data = tr.select_one("td.title")

            # td class="title" 자식중 최초 a 태그안에 제목만 추출
            title = tr_data.select_one("a").text

            # td class="title" 자식중 div 태그 자식중 em 태그에 점수 추출
            point = tr_data.select_one("div.list_netizen_score > em").text

           
            results.append([title, point, writer])
    return results

column = ["영화제목","점수","작성자"]
data = get_movie_point(1,1)

dataframe =  pandas.DataFrame(data, columns=column)
print(dataframe)
dataframe.to_excel("movie.xlsx",
                    sheet_name = "네이버영화",
                    header = True,
                    startrow =0
                    )