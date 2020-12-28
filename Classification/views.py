from django.shortcuts import render, redirect
from Classification.models import Video, Classification
from Start.models import User, Class, Difficulty
import random as rd
from Start import views


def classification_view(request):

    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return redirect("home_name")

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
    print(request.POST)
    if request.method == "POST":
        classification = Classification(
            session_id=User.objects.get(session_id=request.session.session_key),
            video_id=Video.objects.get(video_id=request.POST.get("video_id")),
            class_field=Class.objects.get(label_id=int(request.POST.get("category"))),
            difficulty=Difficulty.objects.get(label_id=int(request.POST.get("difficulty"))),
            play_pause=request.POST.get("play_count"),
            replay=request.POST.get("replay_count"),
            fullscreen=request.POST.get("fullscreen_count"),
            playback=request.POST.get("playback_count"),
            duration_in_sec=request.POST.get("duration"),
            text=request.POST.get("textarea")
        )
        classification.save()
    return render(request, "classification.html", {"video": video})
