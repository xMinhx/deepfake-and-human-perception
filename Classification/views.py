from django.shortcuts import render

def classification_view(request):
    print(request.headers)
    return render(request, "classification.html", {})
