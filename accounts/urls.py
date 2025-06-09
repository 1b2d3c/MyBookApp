from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignupView, MypageView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('mypage/<int:pk>', MypageView.as_view(), name='mypage'),
]