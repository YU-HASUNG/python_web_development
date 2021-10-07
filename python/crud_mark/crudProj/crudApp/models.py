from django.db import models
from django.conf import settings #프로젝트에서 사용하는 유저를 import하기 위해 settings를 가져옴

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    writer = models.CharField(max_length=20, default='닉네임을 입력해주세요') #defalut에 값을 넣어주는 이유는 null값을 방지하기 위해
    body = models.TextField()

    def __str__(self):
        return self.title