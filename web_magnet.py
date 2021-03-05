from flask import Flask  
from flask import render_template
from flask import request
import requests
from bs4 import BeautifulSoup
import re


app = Flask(__name__)  #플라스크 인스턴스 생성

def search_google(keyword, start_pg, end_pg=None):
    url = "https://www.google.com/search?q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet%3A%3Fxt%3D?start={1}".format(keyword,start_pg)
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36,gzip(gfe)"}
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    links = bs.select("div.g > div.rc > div.r > a")

    results = []
    if end_pg is None:  #검색결과 개수 #id명은 #사용
        #counts =bs.select("div#result-stats")[0].text.replace("검색결과 약","").replace("개","").replace(",","").split("(")[0].strip()
        # "검색결과 약" 에서부터 맨 뒤까지 문자열을 슬라이싱 해서 text에 다시 담습니다.
        # "검색결과 약" 이 제거된 text 에서 "개" 를 찾아 그곳까지 슬라이싱해서 다시 text에 담습니다.
        # 최종적으로 , 를 제거하고 공백제거 후 counts 변수에 담으면 숫자만 담겨 집니다.
        parse_text_1 = "검색결과 약"
        parse_text_2 = "개"
        text = bs.select("div#result-stats")[0].text
        text = text[text.find(parse_text_1) + len(parse_text_1):]
        text = text[:text.find(parse_text_2)]
        counts = text.replace(",", "").strip()

        end_pg = int(int(counts)/10)
        if end_pg > 10:
            end_pg = 10

    for a in links:
        href = a["href"]  #링크
        text = a.select("h3")  #제목
        if len(text) <= 0:
            continue #비어있는건 skip
        title = text[0].text
        
        try:
            r = requests.get(href)
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.find_all("a",href=re.compile(r'magnet:\?xt='))   
            #전체 텍스트 주소에서 마그넷 주소 찾기 =findall
            #a링크 전체의  href태그속성에서 마그넷 어쩌고 포함된 속성을 추출
        
            if len(magnets) > 0:
                magnet = magnets[0]["href"]
                results.append({"magnet": magnet},{"title":title})
        except:
            pass
    if start_pg < end_pg:
        start_pg +=10  #규칙때문
        results.extend(search_google(keyword, start_pg, end_pg=end_pg))  #재귀함수

    return results

#웹 표현 route()메소드 사용
@app.route("/", method=["GET", "POST"]) #데코레이터 flask에서는 url연결에 활용 다음 행의 함수부터 데코레이터 적용
def index():
    #return render_template("index.html") #template폴더에서 index.html찾아
    if "keyword" in request.form: #라우터가 실행되고 인덱스 함수가 실행됐을때 전송한 폼
        keyword = request.form["keyword"] #키워드에 해당하는 값(value)
        results=search_google(keyword,0) #키워드로 검색
    else: #키워드가 리퀘스트 폼에 없을떄 (get방식일떄)
        results=[]

    if len(results)>0:  #결과에 무언가 있으면
        return render_template("index.html", **{"magnets":results})#검색 결과를 넘겨줌 딕셔너리 형태
    else:#없으면 검색창 뜨게
        return render_template("index,html")

if __name__ == "__main__": #__+tab키 
    app.run(host="0.0.0.0", port=8765, debug = True) 