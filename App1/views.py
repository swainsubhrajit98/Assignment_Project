from django.shortcuts import render

# Create your views here.
def Website(request):
    return render(request,'Website.html')