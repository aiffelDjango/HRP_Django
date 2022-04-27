from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import HttpResponse
# from urllib3 import HTTPResponse
from stickerUtils.sticker import stickerGen

# Create your views here.
def index(request):
    return render(request, 'Landing/index.html')

def study(request):
    return render(request, 'Landing/study.html')

def test(request):
    return render(request, 'Landing/test.html')

def sticker(req):
    return render(req, 'Landing/sticker.html')

def stickerResult(req):
    # POST
    if req.method == 'POST':
        try:
            imgMemory = req.FILES['image']
            imgByte = imgMemory.read()
            convertImg = "data:image/jpg;base64, "+str(stickerGen(imgByte)) 
            return render(req,'Landing/stickerResult.html',{'image':convertImg})
        except:
            return HttpResponse("보여줄 이미지가 없습니다!")
    # GET
    else:
        return HttpResponse("보여줄 이미지가 없습니다!")