from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post #Post라는 model 생성
        fields = ['title', 'writer', 'body'] #Post라는 model 값 중 받아올 것들