from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate

urlpatterns = [
    path('list/', TodoList.as_view()),
    path('detail/<int:pk>', TodoDetail.as_view()),
    path('create/', TodoCreate.as_view()),
]
