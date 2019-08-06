from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    body = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='(추억이 있는) 사진',upload_to = 'image/', blank = True, null = True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def sum(self):
        return self.body[:50]