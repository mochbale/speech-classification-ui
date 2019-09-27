from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Audio, Text, Grade
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.http import HttpResponseRedirect
import os
from django_project import settings

import time
uploaded_file_list = [];
# Create your views here.
def index(request):
    return render(request, 'django_app/index.html')

def speech_to_text(request):
    data2 = Audio.objects.all()
    return render(request, 'django_app/speech-to-text.html', {"data2" : data2})

def speech_to_text_process(request, pk): #zidane
    data2 = Audio.objects.all()
    text_title = Audio.objects.get(pk=pk).title
    aplicants_name = Audio.objects.get(pk=pk).aplicants_name
    text_audio = Audio.objects.get(pk=pk)

    print("ini text title : ", text_title )
    print("ini apli name : ", aplicants_name )
    print("ini text audio id FK : ", text_audio )

    text = Text(audio=text_audio ,title=text_title, aplicants_name=aplicants_name, full_text="WOI", length="3:33 min")
    text.save()


    return render(request, 'django_app/speech-to-text.html', {"data2" : data2})

def speech_to_text_edit(request):
    return render(request, 'django_app/speech-to-text-edit.html')

def audio_upload(request):
    print(request.method)
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        uploaded_file_list.append(uploaded_file)
        fs = FileSystemStorage()
        audio_name = fs.save(uploaded_file.name, uploaded_file)
        audio_url = fs.url(audio_name)
        audio_byte_size = fs.size(audio_name)/1000000
        audio_megabyte_size = "%.2f" % audio_byte_size
        audio_size = str(audio_megabyte_size)+ " mb"

        audio = Audio(title=audio_name, aplicants_name="Admin (Hard Coded)", directory=audio_url, size=audio_size)
        audio.save()

        print(audio_url)

    data3 = Audio.objects.all()
    return render(request, 'django_app/audio-upload.html', {"data3" : data3})

def text_grading(request):
    data1 = Grade.objects.all()
    return render(request, 'django_app/text-grading.html', {"data1" : data1})

def text_grading_score(request):
    return render(request, 'django_app/text-grading-score.html')

def detail_data(request):
    return render(request, 'django_app/detail-data.html')

def save_audio_bundle(request):
    uploaded_file_list.clear()
    data3 = Audio.objects.all()
    return render(request, 'django_app/audio-upload.html', {"data3" : data3})

def delete_audio(request, pk):
    query = Audio.objects.get(pk=pk)
    audio_title = Audio.objects.get(pk=pk).title
    complete_dir = os.path.join(settings.MEDIA_ROOT, audio_title)
    print("ini base com dir " , complete_dir)
    os.remove(complete_dir)
    query.delete()
    data3 = Audio.objects.all()
    return HttpResponseRedirect(reverse('audio-upload'))

def edit_audio_upload(request, pk):
    audio_title = Audio.objects.get(pk=pk).title
    aplicants_name = Audio.objects.get(pk=pk).aplicants_name

    if request.method == 'POST':
        fs = FileSystemStorage()
        audio = Audio.objects.get(pk=pk)


        audio.title = request.POST['nama-file'] #ini ngambil value dari <input name="nama-file"> di html, trs disimpen ke tabel audio atributenya title
        audio.aplicants_name = request.POST['nama-pelamar'] #ini ngambil value dari <input name="nama-pelamar"> di html, trs disimpen ke tabel audio atributenya aplicants_name
        audio.directory = fs.url(audio.title)


        complete_dir = os.path.join(settings.MEDIA_ROOT, audio_title)
        new_dir = os.path.join(settings.MEDIA_ROOT, audio.title)
        os.rename(complete_dir, new_dir)

        audio.save() #ini ngesave perubahan yang udah dibikin di baris 77 sama 78

        return HttpResponseRedirect(reverse('audio-upload'))

    return render(request, 'django_app/audio-upload-edit.html', {"aplicants_name" : aplicants_name , "audio_title" : audio_title })
