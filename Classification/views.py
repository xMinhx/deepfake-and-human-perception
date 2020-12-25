from django.shortcuts import render
from Classification.models import Video, Classification
import random as rd

def classification_view(request):
    if not request.session.exists(request.session.session_key):
        return render(request, "Start.html")
    video_liste_all = list(Video.objects.values_list('video_id', flat=True))
    video_liste_user = list(Classification.objects.filter(session_id=request.session.session_key))

    for x in video_liste_user:
        if x in video_liste_all:
            video_liste_all.remove(x)
    video_name = rd.choice(video_liste_all)

    video = Video.objects.get(video_id=video_name)
    return render(request, "classification.html", {"video": video})
