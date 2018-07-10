from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def Rankings(request):
    return render(request,"Rankings.html")
