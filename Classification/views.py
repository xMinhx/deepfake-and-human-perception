from django.shortcuts import render
from Classification.models import Video, Classification
from Start.models import User
import random as rd
from Start import views


def classification_view(request):
    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return views.home_screen_view(request)

    user = User.objects.get(session_id=request.session.session_key)
    video_liste_all = []
    video_all_queryset = Video.objects.values_list("video_id")

    for i in range(len(video_all_queryset)):
        video_liste_all.append(video_all_queryset[i][0])

    selected_video = rd.choice(video_liste_all)

    if Classification.objects.filter(session_id=user).exists():

        video_liste_user = []
        video_liste_user_queryset = Classification.objects.filter(session_id=user).values_list("video_id")

        for i in range(len(video_liste_user_queryset)):
            video_liste_user.append(video_liste_user_queryset[i][0])

        for x in video_liste_user:
            if x in video_liste_all:
                video_liste_all.remove(x)
        selected_video = rd.choice(video_liste_all)

    video = Video.objects.get(video_id=selected_video)
    return render(request, "classification.html", {"video": video})
