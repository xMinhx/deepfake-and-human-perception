from django.shortcuts import render, redirect
from Classification.models import Video, Classification
from Start.models import User, Class, Difficulty, Scoreboard
import random as rd


def call_end(request):
    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return render(request, "error page.html")
    user = User.objects.get(session_id=request.session.session_key)
    correct_count = len(Classification.objects.raw('''SELECT c.id, c.session_id_id, c.video_id_id
                                                  FROM public.classification c
                                                  JOIN public.user u ON u.id = c.session_id_id 
                                                  AND u.id = %s
                                                  JOIN video v ON v.video_id = c.video_id_id
                                                  WHERE c.class_field_id = v.label_id''', [user.id]))

    # total_count = len(Classification.objects.raw('''SELECT c.id, c.session_id_id, c.video_id_id
    #                                               FROM public.classification c
    #                                               JOIN public.user u ON u.id = c.session_id_id
    #                                               AND u.id = %s
    #                                               JOIN video v ON v.video_id = c.video_id_id''', [user.id]))
    user_scores = Scoreboard.objects.get(id=1).scores

    if user.id not in user_scores:
        user_scores.update({str(user.id):
                                {"username": "User " + str(user.id),
                                 "correct": correct_count,
                                 "user_score": correct_count * 100}})
        Scoreboard.objects.filter(id=1).update(scores=user_scores)

    return render(request, "endscreen.html", {"user_score": user_scores[str(user.id)]})


def classification_view(request):
    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return render(request, "error page.html")

    user = User.objects.get(session_id=request.session.session_key)
    video_liste_all = [
        "abarnvbtwb.mp4",
        "akvmwkdyuv.mp4",
        "akxoopqjqz.mp4",
        "axoygtekut.mp4",
        "axwovszumc.mp4",
        "bejhvclboh.mp4",
        "bffwsjxghk.mp4",
        "bgwmmujlmc.mp4",
        "bmhvktyiwp.mp4",
        "bntlodcfeg.mp4",
        "bofqajtwve.mp4",
        "bopqhhalml.mp4",
        "bwhlgysghg.mp4",
        "chviwxsfhg.mp4",
        "ckkuyewywx.mp4",
        "clrycekyst.mp4",
        "crktehraph.mp4",
        "cyxlcuyznd.mp4",
        "degpbqvcay.mp4",
        "dhxctgyoqj.mp4",
        "dkuayagnmc.mp4",
        "duycddgtrl.mp4",
        "eckvhdusax.mp4",
        "edyncaijwx.mp4",
        "ellavthztb.mp4",
    ]
    # Replaced with explizit list
    # video_all_queryset = Video.objects.values_list("video_id")

    # for i in range(len(video_all_queryset)):
    # video_liste_all.append(video_all_queryset[i][0])

    if request.method == "POST":
        video_object = Video.objects.get(video_id=request.POST.get("video_id"))
        user_object = User.objects.get(session_id=request.session.session_key)
        if Classification.objects.filter(session_id=user_object, video_id=video_object).exists():
            return redirect("classification_name")
        classification = Classification(
            session_id=user_object,
            video_id=video_object,
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

    selected_video = rd.choice(video_liste_all)
    if Classification.objects.filter(session_id=user).exists():

        video_liste_user = []
        video_liste_user_queryset = Classification.objects.filter(session_id=user).values_list("video_id")

        for i in range(len(video_liste_user_queryset)):
            video_liste_user.append(video_liste_user_queryset[i][0])

        if len(video_liste_user) == 25:
            return call_end(request)

        for x in video_liste_user:
            if x in video_liste_all:
                video_liste_all.remove(x)

        selected_video = rd.choice(video_liste_all)

    video = Video.objects.get(video_id=selected_video)
    return render(request, "classification.html",
                  {"video": video, "videoleft": 25 - len(video_liste_all), "testid": user.testgroup.label_id})


def scores(request):
    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return render(request, "error page.html")

    user_scores = Scoreboard.objects.get(id=1).scores
    sorted_tuple = sorted(user_scores.items(), key=lambda x: x[1]['correct'], reverse=True)
    sorted_dict = {}
    for x in sorted_tuple:
        sorted_dict.update({str(x[0]):
                                {"username": "User " + str(x[0]),
                                 "correct": x[1]["correct"],
                                 "user_score": x[1]["correct"] * 100}})
    user_scores = sorted_dict
    user = User.objects.get(session_id=request.session.session_key)
    return render(request, "scores.html", {"user_scores": user_scores, "user_id": str(user.id)})
