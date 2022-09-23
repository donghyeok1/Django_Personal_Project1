from django.urls import path

from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'), # /accounts/login/ => settings.LOGIN_URL
    # 최상위 루트 페이지는 loginrequired가 적용이 되어있어서 admin에서 로그아웃을 시키고
    # 루트페이지로 가보면 accounts/login url을 따라가게됨
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.profile_edit, name='profile_edit'),
]