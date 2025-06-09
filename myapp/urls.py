from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('books/', views.index_view, name='index'),
    path('books/<int:book_id>/chapters', views.BookView.as_view(), name='book'),
    path('books/<int:chapter_id>/contents', views.ChapterView.as_view(), name='chapter'),
    path('books/<int:content_id>/pages', views.ContentView.as_view(), name='content'),
]