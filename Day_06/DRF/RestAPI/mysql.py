DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql', # 사용할 DBMS
        'NAME' : 'PHR', # Mysql 데이터베이스 이름
        'USER' : 'PHR', # DB 접속 계정명
        'password': 'PHR123', # 해당 계정의 비밀번호
        'HOST' : '146.56.154.230', # IP
        'PORT' : '3306' # PORT
    }
}
