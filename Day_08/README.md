# Day_08 Summary; Deploy (frontend, backend)

- 진행 날짜: 22.05.25
- [작성 참고](https://github.com/kimud6003/KUD/blob/8.Deploy/README/Deploy/8-1.Deploy.md)

## Setting

- 패키지 설치
  - bash web/env.sh
- frontend: node
  - vim web/src/Components/Input 으로 들어가서 파일 수정
    - const URL = '외부IP/sticker/'
    - :wq 로 저장하고 나감
  - npm i
  - npm start
  - 외부IP:3000 으로 접속
- backend: django
  - vim server/server/settings.py 으로 들어가서 파일 수정
    - ALLOWED_HOSTS = ["외부IP"]
    - :wq 로 저장하고 나감
  - python manage.py runserver 0:8000
  - 외부IP:8000 으로 접속
