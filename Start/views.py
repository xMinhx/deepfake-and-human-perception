from django.shortcuts import render
import time
from Start.models import User
from Classification.models import Video, Classification
from Classification import views



# Create your views here.

def home_screen_view(request):
    return render(request, "Start.html", {})


def userdata_view(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    return render(request, "Userdata.html")
