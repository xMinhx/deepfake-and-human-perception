from django.shortcuts import render, redirect
from Classification.models import Video, Classification
from Start.models import User, Class, Difficulty, Testgroup
import random as rd
import json
from django import db
from Start import views

def call_end(request):
    user = User.objects.get(session_id=request.session.session_key)
    correct_count = len(Classification.objects.raw('''SELECT c.id, c.session_id_id, c.video_id_id
                                                  FROM classification c
                                                  JOIN user u ON u.id = c.session_id_id 
                                                  AND u.id = %s
                                                  JOIN video v ON v.video_id = c.video_id_id
                                                  WHERE c.class_field_id = v.label_id''', [user.id]))

    # total_count = len(Classification.objects.raw('''SELECT c.id, c.session_id_id, c.video_id_id
    #                                               FROM classification c
    #                                               JOIN user u ON u.id = c.session_id_id
    #                                               AND u.id = %s
    #                                               JOIN video v ON v.video_id = c.video_id_id''', [user.id]))

    with open("./scores.json", "r") as fp:
        user_scores = json.load(fp)

    if True:
        user_scores.update({str(user.id):
                                {"username" : "User " + str(user.id),
                                "correct": correct_count,
                                 "user_score": correct_count*100}})

        sorted_tuple = sorted(user_scores.items(), key=lambda x: x[1]['correct'], reverse=True)
        sorted_dict = {}
        for x in sorted_tuple:
            sorted_dict.update({str(x[0]):
                                {"username" : "User " + str(x[0]),
                                "correct": x[1]["correct"],
                                 "user_score": x[1]["correct"]*100}})

        with open("./scores.json", "w") as fp2:
            json.dump(sorted_dict, fp2)
    return render(request, "endscreen.html", {"user_score": user_scores[str(user.id)]})


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

        if len(video_liste_user) == 50:
            print("Test")
            return call_end(request)

        for x in video_liste_user:
            if x in video_liste_all:
                video_liste_all.remove(x)

        selected_video = rd.choice(video_liste_all)


    video = Video.objects.get(video_id=selected_video)

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

def scores(request):
    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return redirect("home_name")

    with open("./scores.json", "r") as fp:
        user_scores = json.load(fp)
    user = User.objects.get(session_id=request.session.session_key)
    return render(request, "scores.html", {"user_scores":user_scores, "user_id": str(user.id)})