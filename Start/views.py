from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from Start.models import User, Gender, Testgroup
from django.contrib.sessions.models import Session
import random as rd


# Create your views here.
@csrf_exempt
def home_screen_view(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    return render(request, "Start.html")


def instruction_view(request):
    return render(request, "Introduction.html")


@csrf_exempt
def userdata_view(request):
    if not request.session.exists(request.session.session_key):
        return redirect('')
    if User.objects.filter(session_id=request.session.session_key).exists():

        return redirect("classification_name")

    if request.method == "POST":
        age = int(request.POST.get("age"))
        gender = Gender.objects.get(label_id=request.POST.get("gender"))
        fps = request.POST.get("fps")
        height = request.POST.get("height")
        width = request.POST.get("width")
        testgroup = rd.choice([1, 2])
        new_user = User(session_id=Session.objects.get(session_key=request.session.session_key),
                        gender=gender,
                        age=age,
                        testgroup=Testgroup.objects.get(label_id=testgroup),
                        pixel_height=height,
                        pixel_width=width,
                        fps=fps)
        new_user.save()
        return redirect('classification')
    return render(request, "Userdata.html")
