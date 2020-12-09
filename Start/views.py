from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    print(request.headers)
    return render(request, "Start.html", {})

def user_data_view(request):
    print(request.headers)
    return render(request, "User_data.html", {})