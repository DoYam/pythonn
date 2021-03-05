'''
크롤링 순서
1. 원하는 웹페이지에 접속하여 HTML데이터를 받아온다
2. 받아온 HTML데이터를 분석 가능한 형태로 가공한다
3. 원하는 데이터를 추출한다
'''


import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

""" response = requests.get("https://www.naver.com")
#여기까지 소켓으로 접속해서 데이터를 받아온 거
print(response.status_code)
print(response.headers)
print(response.text)# 디코딩 전 데이터 text , 바이너리 형태 content """ 
bs= BeautifulSoup(response.text,"html.parser")#파싱= 문자열 데이터에서 원하는 요소를 추출하는 것
for img in bs.select("img"):#이미지를 모두 뽑아라
    print(img)
for a in bs.select("a"):
    print(a)

""" session = HTMLSession()
response =session.get("https://www.naver.com")
print(response.html.links)
 """