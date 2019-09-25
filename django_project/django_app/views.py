from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Audio, Text, Grade

# Create your views here.
def index(request):
    return render(request, 'django_app/index.html')

def speech_to_text(request):
    data2 = Text.objects.all()
    return render(request, 'django_app/speech-to-text.html', {"data2" : data2})

def speech_to_text_edit(request):
    return render(request, 'django_app/speech-to-text-edit.html')

def audio_upload(request):
    data3 = Audio.objects.all()
    return render(request, 'django_app/audio-upload.html', {"data3" : data3})

def text_grading(request):
    data1 = Grade.objects.all()
    return render(request, 'django_app/text-grading.html', {"data1" : data1})

def text_grading_score(request):
    return render(request, 'django_app/text-grading-score.html')

def detail_data(request):
    return render(request, 'django_app/detail-data.html')
