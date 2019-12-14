from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoModel

class TodoList(ListView):
    template_name = 'list.html'
    # どのモデルを使用するのか指定してあげないといけない
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    # リダイレクト先の指定
    success_url = reverse_lazy('list')