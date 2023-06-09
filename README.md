# Movie Review & Recommend Site - Replica
> 영화에 대한 커뮤니티와 위시리스트, 검색을 통해 영화 추천 기능을 갖춘 사이트

<br>

### 프로젝트 기간 🗓️
- 2023.05.17 ~ 2023.05.25

<br>

### 개발환경 🛠️
>
> Python 3.9.
> >
> Django 3.2.
> > 
> Node.js 18.
> >
> Vue 2

<br>

## 0. 팀원 🧑‍🤝‍🧑

| 팀원| 역할 | 맡은 분야|
|:---|:---|:---|
|최영태|팀장| 백엔드 위주의 작업 및 프론트 보조|
|김수찬|팀원| 프론트 위주의 작업 및 백엔드 보조|

### 0.1 상세 업무 분담 내역
---
<br>

**공통**: 
- 데이터베이스 모델링 
- 컴포넌트 구조 분석
- 시스템 목업

**최영태**: 
| 개발 분야| 역할 |
|:---:|:---|
|BE| - Django 서버 구현<br> - 영화 리뷰에 대한 데이터 베이스 관리<br> - 사용자의 캐시데이터 기반의 영화 추천 알고리즘 제작 <br> - 코사인유사도를 활용한 영화 추천 알고리즘 제작|
|FE| - 사용자와 관련된 CRUD 서비스 구현<br> - 댓글 페이지 및 댓글창 구현|

**김수찬**:
| 개발 분야| 역할 |
|:---:|:---|
|BE| - 영화 정보에 대한 데이터 관리<br> - 코사인유사도를 활용한 영화 추천 알고리즘 제작|
|FE| - Vue 클라이언트 구현 <br> - 로그인 페이지 디자인<br> - 메인페이지 디자인 <br> - 세부 팝업 디자인|

<br>

## 1. 사용 아키텍쳐 🔗
### 1.1 `Back-End` : Django
---
## ERD 구조
![final_pjt - Database ER diagram (crow's foot)](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/63813952-d2c2-4bce-b43c-ce3731422541)
### **pre - install : Back-End** 
```
$ cd Movie_Review_Site/back-server
$ python –m venv venv
$ source venv/Scripts/activate
$ python install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py loaddata genre_data.json movie_data.json

$ python manage.py runserver
```

### 1.2 `Front-End` : Vue
---
## 컴포넌트 구조
![Image Pasted at 2023-5-26 01-36](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/7e3116d9-4133-4840-b2d6-256ac300c148)

### **pre - install : Front-End** 
```
$ cd Movie_Review_Site/front-server
$ npm install 
$ npm run serve
```

<br>

### 1.3 폴더 구조
---
```
+---back-server
|   +---accounts
|   |   \---migrations
|   +---community
|   |   \---migrations
|   +---final
|   \---movies
|       +---fixtures
|       \---migrations
\---front-server
    +---public
    \---src
        +---api
        |   +---article
        |   +---user
        |   \---movie
        +---assets
        +---layout
        |   \---components
        +---router
        +---store
        |   \---modules
        +---views
        +---components
        |   +---community
        |   +---mainpage
        |   +---modal
        |   \---movie
        \---img
```

### 1.4 DB 구축
---
> TMDB API 이용하여 `약 4600개의 영화` 데이터와 `19개 장르` 데이터 구축<br>
> 감독, 배우 데이터 있는 경우 추가로 입력

<br>

## 2. 개요 📑

### 2.1 목표 서비스
```
    1. 영화 데이터 제공 
    2. 원하는 영화 저장 및 사용자 기반의 영화 추천
    3. 영화 추천 알고리즘 기반의 커뮤니티 서비스 
```
### 2.2 상세 네용
> 0. 시작페이지
```
1. 동적 화면 생성
2. Django Rest-Auth를 활용한 회원가입 / 로그인
3. 로그인 정보에 따른 Navbar 표시 변경
```

> 1. 메인페이지
```
1. 인기 영화에 대한 티저 영상 제공
2. 인기영화 제공
3. 개봉예정작 소개
4. 찜한 목록으로 접근
5. 영화 제공에 대한 시각적인 부분 개선
```

> 2. 영화 추천 서비스
```
1. 유저의 찜 목록을 기반으로 한 영화 추천
2. 영화 장르를 기반으로 한 영화 추천
3. 추천 된 영화목록 중 하나를 랜덤 추출 후 영상 제공
```

> 3. 영화 조회 서비스
```
1. 영화 제목을 기반으로 한 영화 조회
2. 영화 장르를 기반으로 한 영화 조회
3. 개봉 연도를 기반으로 한 영화 조회
4. 검색어에 대한 영화의 유사도를 기반으로 한 영화 조회
5. 검색한 영화와의 유사도를 기반으로한 영화 조회
```

> 4. 커뮤니티 서비스
```
1. 영화 리뷰 및 별점 생성
2. 영화별 리뷰에 대한 접근성을 높임 
3. 게시글을 통해 타 유저의 프로필 확인
4. 리뷰활동을 통해 평점 및 댓글 생성을 통한 의사소통 구현
```

> 5. 개인 프로필 페이지
```
1. 개인간 팔로우 팔로잉 기능
2. 사용자가 찜한 영화 목록 조회
3. 사용자가 생성한 게시글 조회
4. 비밀번호 수정 및 회원탈퇴 기능
```

<br>

## 3. 웹 사이트 예시 📺

### **시작 페이지**
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/451bd058-0f6f-4de2-a37d-a4d561670218)
> 슬라이딩 효과를 통해 로그인 / 회원가입 폼 전환<br>
회원 가입 시 username, nickname, password 입력

<br>

### **메인 페이지**
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/8bb90f08-af2f-48d0-a21d-b0b9643dfe40)
> Navbar를 통한 페이지 이동<br>
마우스 위치에 따라 포스터와 영상 출력

![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/3ba591e5-0475-4a6d-86d8-5a5ea43fda42)
> 인기도 상위 20개, 개봉 예정 영화 20개, 찜 한 영화 목록을 회전 원형으로 나열<br>
포스터 클릭시 상세 정보 모달창 표시

<br>

### **영화 상세 모달**
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/f016c48d-2b5d-45d2-82fd-58cbc403bd41)
> 포스터와 함께 영화 상제 정보 표시<br>
찜하기 버튼으로 찜 리스트에 추가 가능<br>

![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/bd803318-4fbc-4ded-b3df-d80b0b8b9fb6)
> 하단에서 바로 리뷰 작성 가능<br>
별 클릭으로 별점 입력, 입력 칸 더블 클릭으로 리뷰제목 - 리뷰 내용 전환<br>
작성 완료 시 영화 상세 페이지로 이동

<br>

### **영화 상세 페이지**
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/e7cdb9fb-986f-42b7-9f77-f263d9ff57e8)
> 영화 상세 정보와 해당 영화에 작성된 리뷰 나열

![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/9541cb53-c791-4f0e-887b-ebd7827cc15b)
> 하단에 리뷰 작성 폼과 비슷한 장르의 연관 영화 표시

<br>

### **커뮤니티 페이지**
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/c4d9f79b-36cf-4d73-9ba9-17145786bb53)
> 모든 리뷰 조회<br>
각 리뷰 카드의 링크를 통해 영화 상세, 리뷰 상세, 작성자 프로필로 이동 가능

<br>

### **리뷰 상세 페이지**
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/8aa73542-6727-4592-975c-a2330802b0b9)
> 리뷰 내용과 해당 리뷰의 댓글들 표시<br>
댓글 작성 시 비동기적으로 처리되어 새로고침하지 않아도 됨<br> 
닫기 버튼으로 리뷰 & 댓글 창 닫기 가능 <br>
오른쪽엔 해당 영화의 상세 페이지

<br>

### **유저 프로필**
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/2a247629-3c1a-44e5-aff6-bae15006c73a)
> 본인 프로필일 경우 비밀번호 변경 / 회원 탈퇴 활성화<br>
> 해당 유저의 찜 리스트와 작성한 리뷰 조회 가능

![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/348deff9-797d-4899-917c-fd65084cb246)
> 본인 프로필이 아닐 경우 팔로우 버튼 활성화

<br>

### **영화 추천 페이지**
<현재 찜 리스트: 아바타2, 분노의 질주: 라이드 오어 다이, 가디언즈 오브 갤럭시2, 피터팬&웬디>
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/0de3918f-d7f8-43de-91d3-d1c6c3b89329)
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/c699873d-73d9-4d55-8228-0ae2085eced6)
> 찜 리스트 영화의 제목, 장르, 개봉연도, 평점, 인기도, 배우, 감독을 종합적으로 고려하여<br>
코사인 유사도 높은 순으로 영화 추천<br>
캐시 활용하여 같은 찜 리스트에 대해서는 빠른 응답

<br>

### **영화 검색 페이지**

<특정 제목 검색했을 경우>
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/4af59b8c-c8a6-49f7-abc7-88430ffd056d)
<숫자로 검색했을 경우>
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/2d55d1c1-12b6-446d-83b1-e41e9f5ec824)
- 영화제목이 2012인 결과와 개봉연도가 2012년인 영화들

<임의의 키워드 검색했을 경우>
![image](https://github.com/SSAFY-Fianl-PJT/SSAFY-Final-PJT/assets/115714519/0652ada0-1074-47a4-aef4-7fc95decb370)

> 검색어를 제목, 연도, 장르 3가지 모두 필터링 후 종합적으로 출력<br>
TF-IDF 활용하여 overview기반으로 키워드와 연관성 높은 영화 출력<br>
TF-IDF란 ?<br>
문서 내에서 특정 단어의 빈도와 전체 문서 집합에서의 희소성을 고려하여 단어의 중요성을 평가하는 방법

<br>

## 4. 느낀점 및 배운점 💭

**최영태**: 
| | |
|:---:|:---|
|느낀점 | `계획과 현실은 많이 달랐다.`<br>프로젝트를 진행하면서 정말 수많은 에러와 수정사항들을 겪게되었다.<br>프로젝트 시작 당시 조금 막막지만 ERD구성과 figma설계부터 계획을 짜면서<br> 차근차근 나아갔다. 진행 중 초기 구상과 내용이 조금 달라지면서 model수정과 <br>그로 인한 2차 수정들이 연달아 나오게 되었다. 수정을 거듭하면서 초기 구상의 중요성을 깨달을 수 있었다. <br>또한 front와 back 간의 분업이 확실하면서도 협업이 이루어지는 작업과정이 신선했다.<br> back-end 작업이 직접 눈에 보이지 않는 작업들이라 front의 손길이 꼭 필요하다. <br>작업 중에는 보이지 않던 결과가 비로소 눈에 보였을 때의 느낌은 마치 알고리즘을 푸는 것 같았다. <br>작업 중간중간 front 업무를 도와주기도 했지만 역시 나에게는 back-end가 더 잘 맞는다는걸 다시 한번 느끼게 되었다.|
|배운점| <br>영화 추천 알고리즘을 짜면서 `코사인 유사도와 캐싱`을 접하게 되었다.<br> 다른 작업들을 대부분 수업에서 겪었던 것들이었지만 코사인 유사도와 캐싱은 완전 처음 다루어 보게 되었다. <br>코사인 유사도 방법은 영화 상세에 대한 정보들을 추출해서 데이터 프레임을 만든 뒤 데이터들을 벡터 형태로 변환한다 이 과정에서 TF-IDF방식을 사용한다.<br> 벡터화된 정보들간의 코사인 각도를 이용하여 코사인 유사도를 구한다. <br> 유사도를 높은 순으로 나열한 뒤 해당 인덱스의 영화id를 직렬화하여 반환하여 추천 알고리즘을 구현하였다. <br> 하지만 요청마다 이런 계산들을 하기에는 시간적으로 비효율적이었다. <br>그래서 캐싱을 활용하여 이미 계산되었던 값을 저장해놓은 뒤 같은 입력값에 대해 <br>캐시를 이용하여 값에 빠르게 접근하고 계산과정을 생략함으로써 시간을 많이<br> 절약할 수 있었다. (물론 GPT의 도움을 많이 받았다..)|

<br>

**김수찬**:
| | |
|:---:|:---|
|느낀점 | <br>프로젝트를 진행할 때, `컴포넌트의 구성 방식에 따라 장단점`이 있다는 것을 깨달았다. <br> 1.하나의 파일에 모든 로직을 작성할 경우, 개발자의 편의성은 좋아지나, 이후에, 수정 및 보완에 어려움이 심해지고<br> 2. 세분화 하여서 로직을 작성할 경우, 개발자의 편의성은 떨어지지만, 이후에 수정 및 보완이 편해졌다. <br><br> 그런데 또 무작정 좋다고 느껴졌던것 같지도 않았던게, <br> 컴포넌트가 분할되어서 재사용성이 높아졌지만, 이게 뭔가 또 쓸 수 있다 라는 것에 다한 느낌은 별로 안들었다.<br> 대충 컴포넌트 구조 분석을 하면서 5번 쓸 수 있을 것 같았지만 2~3번밖에 못쓴 느낌이였다. <br><br> ++ 미적 감각이 없어서 죽을뻔했다|
|배운점| 알고리즘 풀 때 `모로가도 서울로 가면 된다` 라는 말을 들은 적이 잇다. <br><br> 이 말은 백엔드 보다 프론트에게 더욱 적절하게 적용할 수 있을 것 같다. <br><br> 1. 데이터의 접근 방식 부터 API를 활용하냐 서버를 활용하냐 의 차이<br> 2. 서버를 활용할 때 SSR를 사용하냐 CSR를 사용하냐의 차이<br> 3. CSS를 활용, 하나의 디자인에 여러 방식이 적용 되는 것 까지, <br><br> 알고리즘 푸는 것 보다 멘탈이 더욱 갈렸다...|
