from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import CustomUser

CustomUser = get_user_model()

class CustomUserAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス（※任意）
    '''
    list_display = ('id', 'username', 'password', 'birthday', 'email', 'date_joined') # レコード一覧にid, usernameカラムを表示
    list_display_links = ('id', 'username') # list_displayに指定したカラムにリンクを表示


admin.site.register(CustomUser,CustomUserAdmin)