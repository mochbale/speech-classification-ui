from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Audio(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    aplicants_name = models.CharField(max_length=50)
    directory = models.CharField(max_length=500)
    size = models.CharField(max_length=10)
    length = models.CharField(max_length=10)
    upload_date = models.DateTimeField(default=timezone.now())
    convert_date = models.DateTimeField(blank=True,null=True)

    def convert(self):
        self.convert_date = timezone.now()
        self.text.filter(convert_date=timezone.now())
        self.save()

    def __str__(self):
        return self.title


class Text(models.Model):
    audio = models.ForeignKey('django_app.Audio', related_name='text',on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    aplicants_name = models.CharField(max_length=50)
    full_text = models.TextField(blank=True)
    length = models.CharField(max_length=10)
    convert_date = models.DateTimeField(blank=True,null=True)
    graded_date = models.DateTimeField(blank=True,null=True)

    def convert(self):
        self.convert_date = timezone.now()
        self.save()

    def grade(self):
        self.graded_date = timezone.now()
        self.save()

    def details(self):
        return reverse("this will be the html url",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Grade(models.Model):
    text = models.ForeignKey('django_app.Text', related_name='grade',on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    a_score = models.CharField(max_length=3)
    b_score = models.CharField(max_length=3)
    c_score = models.CharField(max_length=3)
    d_score = models.CharField(max_length=3)
    e_score = models.CharField(max_length=3)
    f_score = models.CharField(max_length=3)
    g_score = models.CharField(max_length=3)
    h_score = models.CharField(max_length=3)
    i_score = models.CharField(max_length=3)
    final_score = models.CharField(max_length=15)

    def __str__(self):
        return self.title
