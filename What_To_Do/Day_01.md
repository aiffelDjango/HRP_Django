# Day_01 Summary; Before Starting Django

- [작성 참고](https://github.com/aiffelDjango/KUD/blob/main/README/Setting/1.Setting.md)

## Python 설치

- [Python 공식 사이트 바로가기](https://www.python.org/downloads/windows/)
- Python 3.8.x 버전 설치
- ![Python 설치 참고](https://github.com/aiffelDjango/KUD/raw/main/README/Setting/img/1.png)

## VS Code 설치

- [VS Code 공식 사이트 바로가기](https://code.visualstudio.com/download)
- 환경 설정은 모두 VS Code Terminal 에서 진행됨

## Python 가상 환경 설정

### 1. 폴더 생성

```bash
mkdir my_django  # 폴더 생성
cd my_django  # 해당 폴더로 이동
```

### 2. 가상환경 설정

- Python venv

```bash
python -m venv myvenv
```

- Anaconda env

```bash
conda create -n my_env python==3.8
```

### 3. 가상환경 사용

- 가상환경 사용

```bash
# Python venv 사용
cd /myvenv/
cd ./Scripts/
./activate

# Anaconda env 사용
conda activate my_env
```

- 가상환경 종료

```bash
# Python venv 종료
deactivate

# Anaconda env 종료
conda deactivate my_env
```

## Django 설치

- pip 업그레이드

```bash
python -m pip install --upgrade pip
pip --version  # pip 22.0.4
```

- Anaconda 업그레이드

```bash
conda update conda
conda update anaconda
conda update -n base conda

conda update --all

conda --version
```

- django 설치

```bash
# pip 로 django 설치
pip install django

# conda 로 django 설치
conda install -c anaconda django
```

## Django 시작

- 프로젝트 시작

```bash
cd ..
cd Django
django-admin startproject firstproject
```

- Django 서버 실행

```bash
cd ./firstproject/
python manage.py runserver
```

- Django 실행 화면

![Django 실행 화면](https://github.com/aiffelDjango/KUD/raw/main/README/Setting/img/4.png)

---

## 참고

### 1. Django Project 폴더 구조

```bash
firstproject
├───manage.py
└───mysite
   ├───__init__.py
   ├───asgi.py
   ├───settings.py
   ├───urls.py
   └───wsgi.py
```

### 2. `.gitignore` 파일 설정

- [gitignore.io](https://www.toptal.com/developers/gitignore) 접속
- django 검색해서 나온 텍스트 모두 복사
- `.gitignore` 파일 생성 후 모두 붙여넣기

### 3. 설치한 패키지 리스트 텍스트 파일 생성

```bash
pip freeze > requirement.txt
```
