"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.urls import path
from Start import views as start
from Classification import views as classification

urlpatterns = [
    path('', classification.scores, name="scores")
    #path('', start.home_screen_view, name="home_name"),
    #path('notification/', start.instruction_view, name="notify_name"),
    #path('userdata/', start.userdata_view, name="userdata_name"),
    #path('classification/', classification.classification_view, name="classification_name"),
    #path('scores/', classification.scores, name="scores")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
