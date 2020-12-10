from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    print(request.headers)
    return render(request, "Start.html", {})

def userdata_view(request):
    print(request.headers)
    return render(request, "Userdata.html", {})

def classification_view(request):
    print(request.headers)
    return render(request, "classification.html", {})