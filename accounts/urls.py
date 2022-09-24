from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'), # /accounts/login/ => settings.LOGIN_URL
    # 최상위 루트 페이지는 loginrequired가 적용이 되어있어서 admin에서 로그아웃을 시키고
    # 루트페이지로 가보면 accounts/login url을 따라가게됨
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    # https://github.com/django/django/blob/main/django/contrib/auth/views.py 에 가서 PasswordChangeView를 볼 것.

    path('signup/', views.signup, name='signup'),
    path('edit/', views.profile_edit, name='profile_edit'),

    re_path(r'^(?P<username>[\w.@+-]+)/follow/$', views.user_follow, name='user_follow'),
    re_path(r'^(?P<username>[\w.@+-]+)/unfollow/$', views.user_unfollow, name='user_unfollow'),
]