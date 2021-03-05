from flask import Flask  
from flask import render_template
from flask import request
import requests
from bs4 import BeautifulSoup
import re


def search_google(keyword, start_pg, end_pg=None):
    url = "https://www.google.com/search?q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet%3A%3Fxt%3D?start={1}".format(keyword,start_pg)
    #실제 특정 브라우저에서 연결하는 것 처럼 구글 서버를 속이는 것
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36,gzip(gfe)"}
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.text, "lxml")
    links = bs.select("div.g > div.rc > div.r > a")

    results = []
    if end_pg is None:  #검색결과 개수 
        #counts =bs.select("div#result-stats")[0].text.replace("검색결과 약","").replace("개","").replace(",","").split("(")[0].strip()
        # "검색결과 약" 에서부터 맨 뒤까지 문자열을 슬라이싱 해서 text에 다시 담습니다.
        # "검색결과 약" 이 제거된 text 에서 "개" 를 찾아 그곳까지 슬라이싱해서 다시 text에 담습니다.
        # 최종적으로 , 를 제거하고 공백제거 후 counts 변수에 담으면 숫자만 담겨 집니다.
        parse_text_1 = "검색결과 약"
        parse_text_2 = "개"
        text = bs.select("div#result-stats")[0].text  #id명은 #사용
        text = text[text.find(parse_text_1) + len(parse_text_1):]
        text = text[:text.find(parse_text_2)]
        counts = text.replace(",", "").strip()

        end_pg = int(int(counts)/10)
        if end_pg > 20:
            end_pg = 20

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
                results.append((title, magnet))
        except:
            pass
    if start_pg < end_pg:
        start_pg +=10  #규칙때문
        results.extend(search_google(keyword, start_pg, end_pg=end_pg))  #재귀함수

    return results

result = search_google("리눅스",0)

for r in result:
    print(r)