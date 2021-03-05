import requests
from bs4 import BeautifulSoup


def get_hotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?q={}".format(keyword)

    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    rows = bs.select("div.resultRow")  #리스트야 포문쓰쟈 

    results=[]
    for r in rows:
        link = r.select("a.dealTitle.bp-c-link")[0]  #["href"]해도 되는데 href없는건 어떡하냐
        href = link.get("href")  #이런식으로 하고 예외처리 ㄱ
        if href is None :  #href없으면
            continue
        href = "https://slickdeals.net" + href
        title = link.text    #제목이랑 링크주소 오케이
        
        #가격정보랑 불아이콘 확인
        price = r.select("span.price")[0].text.replace("$","").replace("from","").strip()
        if price.find("/") >= 0 or price == "":
            continue
        price = float(price)   #달러단위 소수점때문
        hot = len(r.select("span.icon.icon-fire"))

        results.append((title, href, price, hot))
    return results
    
print(get_hotdeal("ipad"))



#미완성 카카오개발자 사이트