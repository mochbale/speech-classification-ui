from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'django_app/index.html')

def speech_to_text(request):
    return render(request, 'django_app/speech-to-text.html')

def speech_to_text_edit(request):
    return render(request, 'django_app/speech-to-text-edit.html')

def audio_upload(request):
    return render(request, 'django_app/audio-upload.html')

def text_grading(request):
    return render(request, 'django_app/text-grading.html')

def text_grading_score(request):
    return render(request, 'django_app/text-grading-score.html')
