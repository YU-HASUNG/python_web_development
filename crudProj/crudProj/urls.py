from django.contrib import admin
from django.urls import path
import crudApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crudApp.views.main, name='main'),
    path('detail/<str:id>', crudApp.views.detail, name='detail'), #특정 id값이 필요하기 때문에 <str:id>달아줌
    path('read/', crudApp.views.read, name = 'read'),
    path('new/create/', crudApp.views.create, name='create'), #create함수 생성으로 기존의 주소를 변경함
    path('edit/<str:id>', crudApp.views.edit, name='edit'),
    path('delete/<str:id>', crudApp.views.delete, name='delete'), #delete함수 경로생성
]
