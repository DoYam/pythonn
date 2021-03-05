'''
import requests
from bs4 import BeautifulSoup

# 2020년 1월 18일 부로 네이버 실시간 검색어 데이터가 페이지 임베딩방식에서
# ajax 통신으로 변경되어서 기존 코드 수정
# 아래 주소가 메인페이지 내부에서 호출되는 실시간 검색어 데이터를 넘겨주는 주소
# request.get("주소").json() 을 하면 데이터를 json 형태로 받아올 수 있습니다.
# 아래 주소를 직접 브라우저에서 접속해보시기 바랍니다.
json = requests.get('https://www.naver.com/srchrank?frm=main').json()

# json 데이터에서 "data" 항목의 값을 추출
ranks = json.get("data")

# 해당 값은 리스트 형태로 제공되기에 리스트만큼 반복
for r in ranks:
    # 각 데이터는 rank, keyword, keyword_synomyms
    rank = r.get("rank")
    keyword = r.get("keyword")
    print(rank, keyword)
'''
import requests
from bs4 import BeautifulSoup
import time

def time_function(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = f(*args,**kwargs)
        end_time = time.time() - start_time
        print("{} {} time {}".format(f.__name__,args[1],end_time))
        return result
    return wrapper

@time_function
 def r_find_all(url,parser):
     r = requests.get(url)
     bs = BeautifulSoup(r.text, parser)
     lists = bs.find_all("li",{"class":"ah_item"})

     titles=[]
     for li in lists:
         title = li.select("span.ah_k")[0].text
         titles.append(title)
         print(titles)
    return titles

@time_function
def r_select(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.select("li.ah_item")

    titles=[]
    for li in lists:
        title = li.select("span.ah_k")[0].text
        titles.append(title)
    return titles

url = "https://www.naver.com"
r_find_all(url,"html.parser")
r_select(url,"html.parser")
r_find_all(url,"lxml")
r_select(url,"lxml")
