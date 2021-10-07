from crudApp.forms import PostForm #form을 사용하기 위해 import 해줌
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone #timezone을 사용하기 위해 import 해줌

# Create your views here.

#메인페이지
def main(request):
    return render(request, 'crudApp/main.html')

#글쓰기페이지
def new(request):
    return render(request, 'crudApp/new.html')

#글쓰기 함수
def create(request): #create 호출
    if request.method == 'POST': #method를 다시 확인
        form = PostForm(request.POST) #입력값 유효성 검증
        if form.is_valid(): #form이 잘 입력되었으면 밑의 과정 실행
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('read') #지정한url 복귀
    else:
        form = PostForm #입력이 잘 되지 않았다면 form을 다시 입력받음
        return render(request, 'crudApp/new.html', {'form':form})

#읽기페이지
def read(request):
    posts = Post.objects #Post의 객체들을 posts라는 변수에 담는다
    return render(request, 'crudApp/read.html', {'posts':posts}) #Post의 객체가 담겨있는 posts라는 변수표현

#디테일페이지
def detail(request, id):
    post = get_object_or_404(Post, id = id) #Post의 객체들을 post라는 변수에 가져온다. id값을 잘 가져오지 못하면 에러발생
    return render(request, 'crudApp/detail.html', {'post':post})

#수정페이지
def edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST": #method를 다시 확인
        form = PostForm(request.POST, instance=post)#입력값 유효성 검증+ 글의 id함수에게 설명해주는 코드
        if form.is_valid():#form이 잘 입력되었으면 밑의 과정 실행
            form.save(commit=False)
            form.save()
            return redirect('read')#지정한url 복귀

    else:
        form = PostForm(instance=post) #입력이 잘 되지 않았다면 form을 다시 입력받음
        return render(request, 'crudApp/edit.html', {'form':form})

#삭제 함수
def delete(request, id): #delete 함수
    post = get_object_or_404(Post, id = id)#Post의 객체들을 post라는 변수에 가져온다. id값을 잘 가져오지 못하면 에러발생
    post.delete() #데이터 삭제
    return redirect('read')#지정한url 복귀