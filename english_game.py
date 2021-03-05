import requests
from bs4 import BeautifulSoup
import re #정규식 라이브러리
import json
import random
import os

def get_news():
    #홈페이지에서 헤드라인 뽑아오자
    url = "https://www.usatoday.com"
    r =requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    lists = bs.select("div.gnt_m_th > a")  #select는 리스트 반환
    for li in lists:
        href = url + li["href"]#주소는 a태그의 href속성
        r = requests.get(href)   #그 주소에서 또 뽑아오자
        bs = BeautifulSoup(r.text, "lxml")
        texts = bs.select("div.gnt_ar_b > p.gnt_ar_b_p")
        contents=[p.text for p in texts]
        contents = " ".join(contents) #인자로 넘어간 리스트가 리스트의 구분을 공백으로 해서 하나의 문자열로 바꿔서 다시 저장
        #str                #리스트
        return contents.lower()  #포문 반복 안해 리턴하려면 함수여야하고
    return None  #오류로 인해서 리스트가 못 구해졌을 때

def naver_translate(word):
    try:
        url = "https://ac.dict.naver.com/enkodict/ac?st=11001&q={}".format(word)
        r = requests.get(url)
        j = json.loads(r.text)
        return (j["items"][0][0][1][0] ) #뜻 그 자체만 추출 리스트속 리스트속 리스트 ...
    except:
        return None
    


#정규식
match_pattern = re.findall(r'\b[a-z]{4,15}\b', get_news()) 
#r은 \를\로 인식하게 해
#\b는 앞뒤의 경계 must\be\happy
#a부터z까지 4자리에서 15자리의 단어
def make_quiz(news):
    frequency = {}
    quiz_list = []

    for word in match_pattern:
        count = frequency.get(word, 0) #없을 수도 있으니까 디폴트값은 0
        frequency[word] = count+1  #워드 키에대한 값 =빈도수 0+1
    

    for word, count in frequency.items():  #key와 value를 한꺼번에 포문 돌려
        if count > 1:
            kor = naver_translate(word)  #한글로 변환 == 네이버사전 크롤링 ...wow
            if kor is not None:
                quiz_list.append({kor : word})  #뜻 : 단어

    return quiz_list



def quiz():  #문제 출력, 게임 실행
    quiz_list = make_quiz(get_news())
    random.shuffle(quiz_list)

    chance = 5
    count = 0

    for q in quiz_list:   #뜻 : 단어
        os.system("cls")  #새로운 퀴즈가 나올 때마다 화면 클리어
        count += 1
        kor = list(q.keys())[0]  #딕셔너리를 리스트로 강제 형변환
        english = q.get(kor)  #값

        print("*"*50)
        print("문제 : {}".format(kor))
        print("*"*50)

        for j in range(chance):
            user_input = str(input("위의 뜻이 의미하는 단어를 입력하세요 > ")).strip().lower()

            if user_input == english:
                print("정답입니다 {}문제 남음".format(len(quiz_list) - count))
                os.system("pause")
                break  #chance를 빠져나가기 위한 포문 클리어후 새로운 문제 ㄱ ㄱ 
            else:
                
                n = chance - (j+1)  #j 0부터 시작
                if j == 0:
                    print("{}가 아닙니다. {} 번 기회가 남았습니다".format(user_input,n))
                elif j == 1:
                    print("{}가 아닙니다 {} 번 기회가 남았습니다 힌트 : {}로 시작".format(user_input, n , english[0]))
                elif j == 2:
                    hint = "  _  "*int(len(english)-2)
                    print("{}가 아닙니다 {} 번 기회가 남았습니다 힌트 : {} {} {}".format(user_input, n, english[0], english[1], hint))
                elif j == 3:
                    hint = "  _  "*int(len(english)-3)
                    print("{}가 아닙니다 {}번 기회가 남았습니다 힌트: {} {} {} {}".format(user_input, n,english[0], english[1],english[2],hint))
                else:
                    print("틀렸습니다! 정답은 {} 입니다".format(english))
                    os.system("pause")
                   
    print("더이상 문제가 없엉")

 quiz()


