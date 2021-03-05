import requests
from bs4 import BeautifulSoup

def get_search_naver_blog(query, start_pg=1, end_pg=None):
    start = (start_pg-1)*10 +1
    url = "https://search.naver.com/search.naver?where=post&query={}&start={}".format(query,start)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    result = []
    if end_pg is None:
        tot_counts = int(bs.select("span.title_num")[0].text.split("/")[-1].replace(",","").replace("건","").strip)
        end_pg =int(tot_counts/10)
        if tot_counts % 10 != 0:
            end_pg +=1

    if end_pg > 900:
        end_pg = 900

    
    lis = bs.select("li.sh_blog_top")
    for li in lis:
        try:
            thumbnail = li.select("img")[0]["src"] #실제 이미지 경로
            summary = li.select("dl > dd.sh_blog_passage")[0].text
            title = li.select("dl > dt > a")[0]
            title_link = title["href"]
            title_text = title.text  

            result.append((thumbnail,title_text, title_link,summary))
        except:
            continue

    if start_pg < end_pg:
        start_pg+=1
        result.extend(get_search_naver_blog(query, start_pg=start_pg,end_pg=end_pg))
    return result

r = get_search_naver_blog("다이어트",start_pg=1, end_pg=3)
print(r)