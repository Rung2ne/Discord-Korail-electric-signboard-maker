# electric-signboard
디스코드 봇으로 전광판 만들기 코드

## requirements
> - discord.py
>> `pip install discord` 
> - pillow.py
>> `pip install pillow`


### PIL(Pillow) 라이브러리는 무엇인가?
- PIL
- Python Imaging Library

파이썬에서 이미지를 다루기 위한 도구 중 하나이다.
이미지를 읽고 쓰는 것은 물론, 크기 조절 및 회전, 필터 적용 등 다양한 것을 할 수 있다.
PIL은 이미지를 **생성**하는 것 또한 가능하다.

PIL은 버려진 지 오래 된 라이브러리다.
Pillow는 그런 PIL의 포크로, 사실상 PIL의 후속 라이브러리이다.

아무튼 위에서 말했듯이 이미지를 **생성**할 수 있으니, 그렇게 전광판 이미지를 만들어 볼 것이다.

[Pillow 라이브러리 공식 문서](https://pillow.readthedocs.io/en/stable/)

## 알아두기
코레일의 플랫폼 내 전광판을 구현하는 것을 우선으로 생각하고 만들었으므로, 색상은 코레일 전광판에 있는 빨강, 주황, 노랑, 초록만 추가해두었고, 폰트는 둥근모꼴+Fixedsys을 사용했습니다.

실제 전광판 폰트도 둥근모꼴입니다.

## 둥근모꼴 폰트 파일 다운하러 가기
[눈누 둥근모꼴+Fixedsys 폰트](https://noonnu.cc/font_page/250)

[바로 둥근모꼴+Fixedsys 폰트 다운하러 가기](https://cactus.tistory.com/193)

안심하세요. 눈누 사이트에 연결된 공식 다운로드 페이지입니다.

## 코드 첨부
[아무튼 코드](https://github.com/Rung2ne/Discord-Korail-electric-signboard-maker/blob/main/app.py)

## 메시지 양식
`<r>빨간색<r/>`
`<g>초록색<g/>`
`<y>노란색<y/>`
`<o>주황색<o/>`

위처럼 두 HTML 태그 사이에 원하는 글자를 넣으시면 됩니다.

한 줄에 15자, 총 4줄이라 60자까지 출력할 수 있습니다.

## 예시 문구 및 이미지
[예시 문구 및 이미지 보러가기](https://github.com/Rung2ne/Discord-Korail-electric-signboard-maker/blob/main/example.md)

## 사용 방법
1. 원하는 폰트를 다운하고 코드에 폰트 경로를 연결해준다.
2. 토큰을 자신의 토큰으로 바꾼다.
3. `pip install pillow`로 PIL 라이브러리를 설치한다.
4. 코드를 실행하고 `/만들기` 명령어로 양식에 맞게 문구를 넣는다. [예시 문구 및 이미지](https://github.com/Rung2ne/Discord-Korail-electric-signboard-maker/blob/main/example.md)를 참고하세요.
