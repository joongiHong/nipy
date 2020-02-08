<p align="center">
    <img src="https://user-images.githubusercontent.com/23215270/74083252-335ccb00-4aa5-11ea-9045-3d87de5c70b2.png" width="500">
    <h1 align="center" style="font-size: 3em;">NiPy</h1>
    <p align="center">
        <img src="https://img.shields.io/badge/python-v3.7-blue">
        <img src="https://img.shields.io/badge/license-MIT-green">
        <img src="https://img.shields.io/badge/test-passing-brightgreen">
    </p>
    <p>NiPy (Neis with ptrhon)이란 대한민국 교육행정정보시스템인 <b>나이스</b>와 관련한 파이썬 개발을 진행하실 때 보다 편리하게 <b>나이스로부터 정보를 가져올 수 있도록 돕는 모듈</b>입니다. 본 모듈은 지금도 개발 중이며 안정성이 보장되지는 않았습니다. 따라서 개발 도중 문제가 발생하시면 이슈 리포트를 이용해 주시거나 직접 소스코드를 수정하여 주시기 바랍니다. 본 모듈은 <b>MIT 라이선스</b>로 자유롭게 사용이 가능합니다.</p>
</p>

<br/>

## 시작하기

NiPy는 다음과 같은 모듈을 사용하기에 반드시 존재하여야 합니다.

- requests
- json
- bs4 (Beautifulsoup)

아래 모듈은 필요시 설치되어야 하는 모듈입니다.

- openpyxl
- csv

위의 모듈들의 설치가 완료되면 본 NiPy의 깃허브 저장소에서 `nipy.py` 파일을 다운받아 원하는 프로젝트가 있는 폴더에 설치하시면 됩니다.

## 사용하기

NiPy는 다음과 같은 기능을 지원합니다.

- 나이스 학교 코드 받아오기 (Scode)
- 학교별 급식 정보 받아오기 (Smeal)
- 학교별 학사 일정 받아오기 (Scalendar)

위와 같은 기능들은 모두 클래스로 이루어져 간단하고 손쉽게 사용하실 수 있습니다. 자세한 사용 방법은 각 api의 문서를 참고하십시오.  
참고로 나이스 홈페이지 개편 등에 의해 지원되지 않을 수 있습니다. 그럴 경우 추후 공개되는 개편안을 확인하여 주십시오.

## 따라하기

NiPy를 활용한 예제는 다음과 같습니다. 사용하기 파트를 통해서도 잘 이해가 되지 않으시거나 NiPy의 모듈이 정상작동 하지 않을 경우 아래의 검증된 코드를 활용하시기 바랍니다.

<details>
    <summary>Scode 활용 예제</summary>

    아래 예제는 경기도내에 있는 김포라는 이름을 가진 학교를 조회하고, 중등 교육기관을 출력받는 예시입니다.

    l = nipy.Scode("김포", "경기")
    print(l.codefind("2"))

    다음과 같이 출력됩니다.

    [{'NAME': '김포신곡중학교', 'ADDRESS': '경기도 김포시 고촌읍 수기로 54-20', 'CODE': 'J100005681'},
    {'NAME': '김포여자중학교', 'ADDRESS': '경기도 김포시 봉화로 37-15', 'CODE': 'J100001488'},
    {'NAME': '김포중학교', 'ADDRESS': '경기도 김포시 봉화로 83', 'CODE': 'J100001490'},
    {'NAME': '김포한가람중학교', 'ADDRESS': '경기도 김포시 김포한강9로 140', 'CODE': 'J100006783'}]

</details>

<details>
    <summary>Smeal 활용 예제</summary>
    
    아래 예제는 경기과학고등학교의 2019년 10월 27일자 중식 급식을 출력하는 예제입니다.

    m = nipy.Smeal("경기", "J100000447", "4")
    print(m.day("2019", "10", "27", "2"))

    다음과 같이 출력됩니다.

    현미밥<br/>김치수제비5.6.9.13.18.<br/>부추겉절이5.6.13.<br/>순살바베큐볶음1.2.5.6.10.13.<br/>배추김치9.13.<br/>푸딩1.<br/>무쌈5.6.9.13.<br/>

</details>

<details>
    <summary>Scalendar 활용 예제</summary>
    
    아래 예제는 경기과학고등학교의 2019년도 9월달 학사 일정을 출력하는 예제입니다.

    c = Scalendar("경기", "J100000447", "4")
    print(c.month("2019", "09"))

    다음과 같이 출력됩니다.

    {'01': '학사일정이 존재하지 않습니다.', '02': '학사일정이 존재하지 않습니다.', '03': '학사일 정이 존재하지 않습니다.', '04': '학사일정이 존재하지 않습니다.', '05': '학사일정이 존재하지  않습니다.', '06': '학사일정이 존재하지 않습니다.', '07': '토요휴업일', '08': '학사일정이 존재하지 않습니다.', '09': '학사일정이 존재하지 않습니다.', '10': '학사일정이 존재하지 않습니다.', '11': '학사일정이 존재하지 않습니다.', '12': '추석', '13': '추석', '14': '추석', '15': '학 사일정이 존재하지 않습니다.', '16': '학사일정이 존재하지 않습니다.', '17': '학사일정이 존재하지 않습니다.', '18': '학사일정이 존재하지 않습니다.', '19': '학사일정이 존재하지 않습니다.', '20': '학사일정이 존재하지 않습니다.', '21': '토요휴업일', '22': '학사일정이 존재하지 않습니 다.', '23': '학사일정이 존재하지 않습니다.', '24': '학사일정이 존재하지 않습니다.', '25': '학사일정이 존재하지 않습니다.', '26': '학사일정이 존재하지 않습니다.', '27': '학사일정이 존재하지 않습니다.', '28': '토요휴업일', '29': '학사일정이 존재하지 않습니다.', '30': '학사일정이  존재하지 않습니다.'}

</details>

아래는 실제 프로젝트에 NiPy 모듈이 적용된 예시입니다.

- [Yami! (학교 급식을 불러오는 프로그램)](https://github.com/joongiHong/yami)

## 라이선스 보기

본 모듈의 라이선스는 `MIT LICENSE`입니다.  
따라서 본 모듈을 사용한 모든 프로젝트는 아래의 조건을 준수할 경우 배포, 수정, 상업적 이용을 포함한 모든 행위가 허가됩니다.

> 반드시 출처를 표시해야 합니다.  
> 본 프로젝트의 출처는 본 저장소의 url 주소나 Joongi Hong 혹은 홍준기입니다.

또한 본 모듈에 활용된 오픈소스은 다음과 같습니다.

- [Requests](https://2.python-requests.org/en/master/user/intro/#apache2-license)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/)

위의 오픈소스를 제공해 주셔서 다시 한번 감사드립니다.

## 문의하기

본 모듈에 관하여 물어보실 내용은 본 저장소의 이슈 레포트를 활용하여 주십시오.

본 모듈의 개발 과정에 대한 문의는 [블로그](joongi0405.tistory.com)를 방문해 주십시오.

본 모듈이 아닌 개인적인 문의나 기타 문의의 경우 아래 이메일 주소를 활용해 주십시오.

- joongi1978@naver.com
- joongi2006@kakao.com
