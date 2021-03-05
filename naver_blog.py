import requests
from bs4 import BeautifulSoup


def get_search_naver_blog(query, start_pg=1, end_pg=None):
    start = (start_pg - 1)*10 + 1
    url = "https://search.naver.com/search.naver?where=post&query={}&start={}".format(query,start)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")  #파싱 완료

    result=[]

    #1-10 / 9,147건
    if end_pg is None:
        tot_counts = int(bs.select("span.title_num")[0].text.split("/")[-1].replace("건","").replace(",","").strip)
        end_pg = tot_page = int(tot_counts/10)
        if tot_counts %10 >0:
            end_pg+=1

    if end_pg > 900:
        end_pg = 900

    lis = bs.select("li.sh_blog_top")
    for li in lis:
        try:
            thumbnail = li.select("img")[0]["src"]  #이미지 경로=src속성 값 예외처리 생략
            summary = li.select("dl > dd.sh_blog_passage")[0].text

            title = li.select("dl > dt > a")[0]   #select는 리스트형태
            title_link= title["href"]    #<a href ="링크"
            title_text= title.text
            
            result.append((thumbnail, title_text, title_link, summary))  #리스트에 결과를 append
        except:
            continue
        
    if start_pg < end_pg:
        start_pg +=1
        result.extend(get_search_naver_blog(query, start_pg= start_pg, end_pg=end_pg))  #리스트에 리스트를extend, 재귀함수

    return result

results = get_search_naver_blog("다이어트", start_pg=1, end_pg =1 )
for result in results:
    print(result)