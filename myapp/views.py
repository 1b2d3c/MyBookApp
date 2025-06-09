from django.core.paginator import Paginator
from .consts import ITEM_PER_PAGE
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Books, Chapters, Contents, Pages
from django.db.models import Avg
from .forms import SearchForm

class TopView(LoginRequiredMixin, ListView):
    template_name = 'myapp/top.html'
    model = Books

def index_view(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        object_list = Books.objects.filter(title__contains=keyword)
    else:
        searchForm = SearchForm()
        object_list = Books.objects.all()
    return render(request, 'myapp/index.html',{'searchForm': searchForm, 'object_list': object_list},)

class BookView(LoginRequiredMixin, ListView):
    template_name = 'myapp/book.html'
    model = Chapters

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['chapters_list'] = Chapters.objects.filter(book=self.kwargs['book_id'])
        context['book'] = Books.objects.get(pk=self.kwargs['book_id'])
        return context

class ChapterView(LoginRequiredMixin, ListView):
    template_name = 'myapp/chapter.html'
    model = Contents

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['contents_list'] = Contents.objects.filter(chapter=self.kwargs['chapter_id'])
        context['chapter'] = Chapters.objects.get(pk=self.kwargs['chapter_id'])
        return context

class ContentView(LoginRequiredMixin, ListView):
    template_name = 'myapp/content.html'
    model = Pages

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['pages_list'] = Pages.objects.filter(contents=self.kwargs['content_id'])
        context['content'] = Contents.objects.get(pk=self.kwargs['content_id'])
        return context