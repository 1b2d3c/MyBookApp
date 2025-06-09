from django.contrib import admin
from .models import Books, Chapters, Contents, Pages

admin.site.register(Books)
admin.site.register(Chapters)
admin.site.register(Contents)
admin.site.register(Pages)