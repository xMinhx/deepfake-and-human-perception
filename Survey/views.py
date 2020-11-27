from django.shortcuts import render

# Create your views here.
def exercise_screen(request):
    print(request.headers)
    return render(request, "Exercise.html", {})