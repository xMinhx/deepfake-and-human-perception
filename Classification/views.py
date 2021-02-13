from django.shortcuts import render, redirect
from Classification.models import Video, Classification
from Start.models import User, Class, Difficulty, Scoreboard
import random as rd

#Is called when user classified all videos
def call_end(request):
    #Check if user exist in database
    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return render(request, "error page.html")
    
    #Get the user instance by session key
    user = User.objects.get(session_id=request.session.session_key)
    
    #Calls all instance of correct classification data set from the user
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
    
    #Calls the scoreboard from database
    user_scores = Scoreboard.objects.get(id=1).scores

    #If user doesen't exist in scoreboard add him
    if user.id not in user_scores:
        user_scores.update({str(user.id):
                                {"username": "User " + str(user.id),
                                 "correct": correct_count,
                                 "user_score": correct_count * 100}})
        Scoreboard.objects.filter(id=1).update(scores=user_scores)

    return render(request, "endscreen.html", {"user_score": user_scores[str(user.id)]})

#Is called upon entering the classification process
def classification_view(request):
    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return render(request, "error page.html")
    
    #Get instance of the user based on his session key
    user = User.objects.get(session_id=request.session.session_key)
    
    #List of all videos used for classification
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
    
    #Is called if the submit button has been pressed
    if request.method == "POST":
        video_object = Video.objects.get(video_id=request.POST.get("video_id"))
        user_object = User.objects.get(session_id=request.session.session_key)
        
        #Check if user already classified the video if yes, call new video
        if Classification.objects.filter(session_id=user_object, video_id=video_object).exists():
            return redirect("classification_name")
        
        #Generate new classification dataset based on the information submitted by the user and the front-end
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

    #Choose random video from all videos
    selected_video = rd.choice(video_liste_all)
    
    #If user already classified atleast one video, calculate the difference and choose a video from that list
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

#Is called if user visits scoreboard
def scores(request):
    #Check if user already exist
    if (not request.session.exists(request.session.session_key)) or (
            not User.objects.filter(session_id=request.session.session_key).exists()):
        return render(request, "error page.html")
    
    #Calls scoreboard from database
    user_scores = Scoreboard.objects.get(id=1).scores
    
    #Sorts the scorboard based on correct answers DESC
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
