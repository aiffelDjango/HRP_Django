# Day_05 Summary; SQL

- 진행 날짜: 22.05.04
- [작성 참고](https://github.com/aiffelDjango/KUD/blob/main/README/SQL/5.SQL.md)

## Setting

### [MySQL Workbench 설치](https://dev.mysql.com/downloads/workbench/)

- [mysql-workbench-community-8.0.29-winx64.msi](https://dev.mysql.com/downloads/file/?id=510444)

### MySQL Workbench 실행 후 서버 연결

- Setup New Connection

|N|Contents|작성|
|:---:|:---:|:---:|
|1|Connection Name|PHR|
|2|Hostname|IP주소|
|3|Username|PHR|
|4|Password|PHR123|

## SQL

### 데이터 타입 [참고](http://www.tcpschool.com/mysql/mysql_datatype_numeric)

|타입|설명|
|:---:|:---:|
|INT|정수형|
|DOUBLE|실수형|
|VARCHAR|가변 문자열|
|TEXT|기본값 설정 불가능, 가변 문자열|
|DATETIME|날짜, 시간|

### CRUD

||설명|
|:---:|:---:|
|C|Create|
|R|Read|
|U|Update|
|D|Delete|

#### ERD(Entity Relationship Diagram)

![](https://github.com/aiffelDjango/KUD/raw/main/README/SQL/img/RDB.jpeg)

#### Create; INSERT

```sql
-- Users 테이블 생성
CREATE TABLE PHR.Users(
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
  first_name VARCHAR(255) NOT NULL,
  birthday DATETIME NOT NULL DEFAULT '2022.5.4'
);

-- 값 추가 방식 1: 모든 컬럼값 추가
INSERT INTO PHR.Users
VALUES('0', 'Park','2022.5.4'); -- AUTO_INCREMENT 라서 '0' 으로 설정한 것과 상관없이 자동으로 증가값이 입력됨

-- 값 추가 방식 2: 원하는 컬럼값만 추가
INSERT INTO PHR.Users(first_name)
VALUES('Park');
```

|설정|설명|
|:---:|:---:|
|NOT NULL|입력할 때 해당 컬럼값 무조건 받음|
|PRIMARY KEY|해당 컬럼값은 반드시 존재(NOT NULL) & 유일(UNIQUE)해야 함|
|AUTO_INCREMENT|자동 값 증가|
|UNIQUE|중복 허용X|
|DEFAULT '값'|기본값 설정|

#### Read; SELECT

1. 기본

```sql
-- 전체 데이터 보기
SELECT * FROM PHR.Users;

-- 원하는 컬럼만 보기
SELECT first_name FROM PHR.Users;

-- 조건을 토대로 데이터 찾기
SELECT * FROM PHR.Users WHERE id > 1;
```

2. GROUP BY

```sql
-- 특정 컬럼 그룹화
SELECT birthday, COUNT(*)
FROM PHR.Users
GROUP BY birthday;
```

|종류|설명|
|:---:|:---:|
|COUNT|개수 세기|
|MIN|최솟값|
|MAX|최댓값|
|SUM|합|
|AVG|평균|

3. ORDER BY

```sql
-- 오름차순 정렬
SELECT * FROM PHR.Users ORDER BY birthday ASC;

-- 내림차순 정렬
SELECT * FROM PHR.Users ORDER BY birthday DESC;
```

4. LIKE

```sql
-- 부분적으로 일치하는 문자열 검색 => 'L%': L로 시작하는 문자열 모두 찾아냄
SELECT * FROM PHR.Users WHERE first_name LIKE 'L%';

-- 문자열 길이 정확히 일치하는 문자열 검색 => 'L__': L로 시작하는 세 글자 문자열 찾아냄
SELECT * FROM PHR.Users WHERE first_name LIKE 'L__';
```

5. JOIN

```sql
-- Movies 테이블 생성
CREATE TABLE PHR.Movies(
 id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENTint,
    title TEXT NOT NULL,
    first_name VARCHAR(255) NOT NULL
)
```

![](https://github.com/aiffelDjango/KUD/raw/main/README/SQL/img/6.png)

```sql
-- JOIN 결과: count(Movies)*count(Users)
SELECT * FROM PHR.Movies JOIN PHR.Users;

-- INNER JOIN 결과: Movies ∩ Users
SELECT * FROM PHR.Movies JOIN PHR.Users WHERE Movies.first_name = Users.first_name;

-- LEFT JOIN 결과: Movies ⊃ (Movies ∩ Users)
SELECT * FROM PHR.Movies LEFT JOIN PHR.Users ON Movies.first_name = Users.first_name;

-- RIGHT JOIN 결과: (Movies ∩ Users) ⊂ Users
SELECT * FROM PHR.Movies RIGHT JOIN PHR.Users ON Movies.first_name = Users.first_name;
```

#### Update; UPDATE

```sql
-- 데이터 수정하려면 WHERE 조건 필요
UPDATE PHR.Users
SET first_name = 'Park'
WHERE id = 1;
```

#### Delete; DELETE

```sql
-- 행 삭제
DELETE FROM PHR.Users WHERE id = 1;
```
