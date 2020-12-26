from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Start.models import User, Gender, Testgroup
from django.contrib.sessions.models import Session
from Classification.models import Video, Classification
from Classification import views
import random as rd


# Create your views here.
@csrf_exempt
def home_screen_view(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    return render(request, "Start.html")


@csrf_exempt
def userdata_view(request):
    if not request.session.exists(request.session.session_key):
        return home_screen_view(request)
    response = render(request, "Userdata.html")
    if User.objects.filter(session_id=request.session.session_key).exists():
        response = views.classification_view(request)

    if request.method == "POST":
        if (request.POST.get("age") or request.POST.get("gender")) is None:
            response = render(request, "Userdata.html")
        else:
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
            response = views.classification_view(request)
    return response



