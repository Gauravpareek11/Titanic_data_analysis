from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def result(request):
    p_id=request.GET['passenger_id']
    print(p_id)
    return render(request,'result.html')