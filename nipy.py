'''

[NiPy]

대부분의 코드에는 주석이 포함되어 있습니다.
Github 문서와 주석을 참고하여 필요한 코드만 살려
경량화 하시기 바랍니다.

'''

# ~~ 0. 임포트 부분 ~~
import requests  # (필수) 나이스 서버와 통신용
import json  # (필수) api 사용시 파싱용
from bs4 import BeautifulSoup  # (필수) 나이스 페이지 파싱용


# ~~ 1. 학교 코드를 불러오는 api ~~

class Scode:  # Scode 클래스 생성
    def __init__(self, name, city):  # 학교 이름과 위치를 받아옴
        city_dict = {"서울": "1100000000", "부산": "2600000000", "대구": "2700000000",
                     "인천": "2800000000", "광주": "2900000000", "대전": "3000000000",
                     "울산": "3100000000", "세종": "3600000000", "경기": "4100000000",
                     "강원": "4200000000", "충북": "4300000000", "충남": "4400000000",
                     "전북": "4500000000", "전남": "4600000000", "경북": "4700000000",
                     "경남": "4800000000", "제주": "5000000000"}  # 지역 목록

        self.city = city_dict.get(city, "nocity")  # 지역 코드로 변환
        self.name = name  # 학교 이름 저장

    def codefind(self):  # 실질적으로 코드를 반환하는 부분
        url = "https://www.schoolinfo.go.kr/ei/ss/Pneiss_a01_10.do"  # 학교알리미 코드 불러오는 주소
        para = {"SIDO_CODE": self.city, "SRC_HG_NM": self.name}  # post 파라미터

        re = requests.post(url, data=para)  # 서버 접속

        if re != "200":
            return("SERVER ERROR")


# ~~ 2. 학교 급식을 불러오는 api ~~

class Smeal:  # 클래스
    def __init__(self, ooe, code, year, month, day, sclass, kind):  # 초기화자 메서드 선언
        self.ooe = ooe  # 교육청
        self.year = year  # 조회 년월일
        self.month = month
        self.il = day
        self.ymd = year + "." + month + "." + day
        self.sclass = sclass  # 교급
        self.kind = kind  # 조회 급식 종류
        self.code = code  # 학교 고유 코드

    def day(self):  # 하루치 급식을 조회
        if type(self.ooe) != str or type(self.ymd) != str or type(self.sclass) != str\
                or type(self.kind) != str or type(self.code) != str:
            return("TYPE ERROR")

        if len(self.year) != 4 or len(self.month) != 2 or len(self.il) != 2\
                or len(self.sclass) != 1 or len(self.kind) != 1:
            return("SIZE ERROR")

        url = "http://stu." + self.ooe + ".go.kr/sts_sci_md01_001.do?" +\
            "schulCode=" + self.code +\
            "&schulCrseScCode=" + self.sclass +\
            "&schulKnaScCode=0" + self.sclass +\
            "&schMmealScCode=" + self.kind +\
            "&schYmd=" + self.ymd  # 나이스 학교 급식 조회 주소

        response = requests.get(url)  # 급식 정보 조회
        if response.status_code != 200:  # 응답이 200 (정상응답)이 아닐경우
            return('SERVER ERROR')  # 에러 반환

        foodhtml = BeautifulSoup(response.text, 'html.parser')  # 급식정보 파싱 준비
        foodhtml_data_tr = foodhtml.find_all('tr')  # 모든 tr태그 불러오기

        # 몇번째 행에 급식 정보가 존재하는지 구분하는 로직

        foodhtml_data = foodhtml_data_tr[0].find_all('th')  # 날짜 정보가 있는 열을 불러옴

        try:  # 예외 처리를 위한 try
            for i in range(1, 7):  # 월요일부터 일요일까지 하나하나 대입 준비
                date = str(foodhtml_data[i])  # i요일째 날짜 정보 확인
                date_filter = ['<th class="point2" scope="col">', '<th class="last point1" scope="col">',
                               '<th scope="col">', '</th>', '(', ')', '일', '월', '화', '수', '목', '금', '토']  # 제거해야 하는 목록

                for sakje in date_filter:
                    date = date.replace(sakje, '')  # 찌끄레기를 삭제

                if date != self.ymd:  # 날짜와 입력날짜 동일 여부 확인
                    continue

                hang = i - 1  # 급식정보가 존재하는 행 선언
                break  # 존재 확인 로직 정지

        except:  # 에러 발생시 데이터베이스 에러 반환
            return("NO DATABASE")

        # 급식 정보 조회 시작

        try:
            food = foodhtml_data_tr[2].find_all(
                'td')  # 급식정보가 있는 행의 모든 td 태그 불러오기
            food = str(food[hang])  # hang 번째에 있는 급식 정보 불러옴

            food_filter = ['<td class="textC">',
                           '<td class="textC last">', '</td>']  # 제거해야 하는 목록

            for sakje in food_filter:
                food = food.replace(sakje, '')  # 찌끄레기를 삭제

            if food == ' ':
                food = '급식이 예정되지 않았거나 정보가 존재하지 않습니다.'  # 만약 조회시 급식정보가 없다면 미존재 안내

        except:
            food = 'NO DATABASE'  # 급식 조회 실패시 안내

        return(food)  # 정보 반환
