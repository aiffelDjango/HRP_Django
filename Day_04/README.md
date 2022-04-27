# Day_04 Summary; StickerUtils with dlib

- 진행 날짜: 22.04.27
- [작성 참고](https://github.com/aiffelDjango/KUD/blob/main/README/Sticker/4.Sticker.md)
- AIFFEL/EXPLORATION_03

## Setting

- 라이브러리 설치
  - 주의사항: 반드시 cmake 먼저 설치하고 dlib 을 설치해야 함!
  - dlib 설치가 제대로 안 될 경우, 시도할 수 있는 방법
    1) 아나콘다 사용자: conda install -c conda-forge dlib
    2) visual studio 설치, dlib 파일 직접 받아서 설치 [[참고1]](https://daily-error.tistory.com/55) [[참고2]](https://updaun.tistory.com/entry/python-python-37-dlib-install-error)
    3) pip 업그레이드: python -m pip install --upgrade pip
    4) CMake 사용해서 직접 빌드 [[참고1]](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=os2dr&logNo=221818707061) [[참고2]](https://m.blog.naver.com/dic1224/221069482304)

```bash
pip install opencv-python
pip install matplotlib
pip install cmake
pip install dlib
```

- 이미지 다운로드
  - 사람 이미지 다운로드
    - 위치: StickerUtils/images/Image.png
    - 본인 사진 가능
    - 연예인 사진 가능
  - [sticker 다운로드](https://drive.google.com/file/d/1knZtRmrsXVqYutibA9O06QVhFXb4oWl4/view)
    - 위치: StickerUtils/images/king.png
- 모델 다운로드
  - [dlib face landmark 모델 다운로드](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
    - 위치: StickerUtils/models/shape_predictor_68_face_landmarks.dat

## StickerUtils

- 동작 과정

|서버 실행|이미지 선택|스티커 붙이기|
|:---:|:---:|:---:|
|![실행_1][실행_1]|![실행_2][실행_2]|![실행_3][실행_3]|

[실행_1]: https://github.com/aiffelDjango/KUD/raw/main/README/Sticker/img/1.png
[실행_2]: https://github.com/aiffelDjango/KUD/raw/main/README/Sticker/img/2.png
[실행_3]: https://github.com/aiffelDjango/KUD/raw/main/README/Sticker/img/3.png

- 폴더 구조

```bash
fristproject
├───config
├───Landing
├───static
├───templates
└───stickerUtil
    ├───sticker.py
    ├───images
    │   ├─── image.png
    │   └─── king.png
    └───models
        └───shape_predictor_68_face_landmarks.dat
```

- templates/Landing/sticker.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Sticker AI view</title>
  </head>
  <body>
    <div>
      <!-- img 태그로 이미지 데이터 그 자체를 보내려면 base64 형식이어야만 가능함 -->
      <img src="{{ image }}" style="width: 40vw" alt="convertImage" />
    </div>
  </body>
</html>
```

- templates/Landing/stickerResult.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Sticker AI</title>
  </head>
  <body>
    <div class="container">
      <!-- form action을 통해 이미지가 전송이 되었을때 처리할 내용물이 전달이 되면 페이지 이동-->
      <!-- action 설정 => Landing.views.stickerResult 페이지 연결 -->
      <form
        method="POST"
        action="{% url 'stickerResult' %}"
        enctype="multipart/form-data"
      >
        {% csrf_token %}
        <input type="file" name="image" /><br />
        <input type="submit" value="테스트 해보기 " />
      </form>
    </div>
  </body>
</html>
```

- Landing/views.py

```python
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import HttpResponse
from stickerUtils.sticker import stickerGen


def sticker(req):
    return render(req,'Landing/sticker.html')

def stickerResult(request):
    if request.method == 'POST': # 통신이 post일 때
        try:
            imgMemory = req.FILES['image']
            imgByte = imgMemory.read()  # 통신에서 image 불러오기
            convertImg = "data:image/jpg;base64, "+str(stickerGen(imgByte))  # 인공지능 코드 추가
            return render(request, 'Landing/stickerResult.html', {'image':convertImg})  # stickerResult.html을 보여줄때 가공한 image 파일(=스티커를 붙인 결과 이미지)도 같이 넘김
        except:
            return   HttpResponse("보여줄 이미지가 없습니다!")  # image 파일이 없으면 처리
    else:  # 통신이 get일 때
        return   HttpResponse("보여줄 이미지가 없습니다!")  # post 통신이 아니면 자료를 보낼수 없어서 예외 처리
```

- config/urls.py

```python
from django.contrib import admin
from django.urls import path
import Landing.views

urlpatterns = [
    path('sticker',Landing.views.sticker,name="sticker"),  # 스티커를 붙이고 싶은 이미지를 입력하는 페이지
    path('stickerResult',Landing.views.stickerResult,name="stickerResult")  # 스티커를 붙인 결과 이미지를 보여주는 페이지
]
```

- stickerUtils/sticker.py

```python
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import dlib
import base64

file_dir = os.path.dirname(__file__)

# views.py 에서 POST 로 받은 img 를 처리함
def stickerGen(img):
    # 이미지 데이터 디코딩(base64 -> np.uint8)
    # cf. 통신으로 받은 image(=img 태그로 받은 이미지 데이터 그 자체, base64 형식)를 작업하려면 디코딩 필요
    img_bgr = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_UNCHANGED)
    detector_hog = dlib.get_frontal_face_detector()

    # 이미지 불러오기
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    dlib_rects = detector_hog(img_rgb, 1)

    # 모델 불러오기
    model_path = file_dir+'/models/shape_predictor_68_face_landmarks.dat'
    landmark_predictor = dlib.shape_predictor(model_path)

    # 얼굴 영역 박스마다 face landmark 찾기
    list_landmarks = []
    for dlib_rect in dlib_rects:
        points = landmark_predictor(img_rgb, dlib_rect)
        list_points = list(map(lambda p: (p.x, p.y), points.parts()))  # face landmark 저장
        list_landmarks.append(list_points)

    # 스티커 붙일 좌표, 스티커 크기 초기값 설정
    for dlib_rect, landmark in zip(dlib_rects, list_landmarks):
        x = landmark[30][0]
        y = landmark[30][1] - dlib_rect.height()//2
        w = h = dlib_rect.width()

    # 스티커 크기 조절
    sticker_path = file_dir+'/images/king.png'
    img_sticker = cv2.imread(sticker_path)
    img_sticker = cv2.resize(img_sticker, (w,h))

    # 스티커 위치 조절
    refined_x = x - w // 2
    refined_y = y - h

    # 스티커 위치 넘어가면 잘리게 함
    if refined_x < 0:
        img_sticker = img_sticker[:, -refined_x:]
        refined_x = 0
    if refined_y < 0:
        img_sticker = img_sticker[-refined_y:, :]
        refined_y = 0

    # 이미지에 스티커 적용
    sticker_area = img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]]
    img_bgr[refined_y:refined_y +img_sticker.shape[0], refined_x:refined_x+img_sticker.shape[1]] = \
        np.where(img_sticker==0,sticker_area,img_sticker).astype(np.uint8)

    # 이미지 데이터 인코딩/디코딩(jpg -> base64 -> utf-8)
    # cf. stickerResult 페이지를 보여주기 위해 stickerResult.html과 가공한 image 파일(=스티커를 붙인 결과 이미지)를 같이 넘김
    img_bgr_buffer = cv2.imencode('.jpg', img_bgr)[1]
    result = base64.b64encode(img_bgr_buffer).decode("utf-8")
    return result
```
