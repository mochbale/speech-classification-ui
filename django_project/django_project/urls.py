"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^index.html$',views.index, name='index'),
    url(r'^speech-to-text.html$',views.speech_to_text, name='speech_to_text'),
    url(r'^speech-to-text-edit.html$',views.speech_to_text_edit, name='speech_to_text-edit'),
    url(r'^audio-upload.html$',views.audio_upload, name='audio-upload'),
    url(r'^text-grading.html$',views.text_grading, name='text grading'),
    url(r'^text-grading-score.html$',views.text_grading_score, name='text grading-score'),
    url(r'^detail-data.html$',views.detail_data, name='detail-data'),
    url(r'^django_app',include('django_app.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
