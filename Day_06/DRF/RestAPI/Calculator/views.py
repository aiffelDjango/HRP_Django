from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView

# Create your views here.
@api_view(['GET'])
def hello(request):
    if request.method == 'GET':
        return Response("Hello")

@api_view(['GET', 'POST'])
def calc_add(request):
    if request.method == 'GET':
        return Response("This Method is PLUS")
    
    if request.method == 'POST':
        num1 = request.data["number1"]
        num2 = request.data["number2"]
        return Response(num1 + num2)
    
        # {
        # "number1":1,
        # "number2":10
        # }

@api_view(['GET', 'POST'])
def calc_sub(request):
    if request.method == 'GET':
        return Response("This Method is SUB")
    
    if request.method == 'POST':
        num1 = request.data["number1"]
        num2 = request.data["number2"]
        return Response(num1 - num2)
    
@api_view(['GET', 'POST'])
def calc_mul(request):
    if request.method == 'GET':
        return Response("This Method is MUL")
    
    if request.method == 'POST':
        num1 = request.data["number1"]
        num2 = request.data["number2"]
        return Response(num1 * num2)
    
@api_view(['GET', 'POST'])
def calc_div(request):
    if request.method == 'GET':
        return Response("This Method is DIV")
    
    if request.method == 'POST':
        num1 = request.data["number1"]
        num2 = request.data["number2"]
        return Response(num1 / num2)
    
class class_add(APIView):
    
    def get(self, request):
        return Response("ADD")
    
    def post(self, request):
        number1 = request.data["number1"]
        number2 = request.data["number2"]
        return Response(number1+number2)