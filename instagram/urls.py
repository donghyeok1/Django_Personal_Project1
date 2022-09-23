from django.urls import path, re_path
from django.contrib.auth.validators import UnicodeUsernameValidator
from instagram import views

app_name = 'instagram'

#     username을 url로 쓰기 위해서
#     https://github.com/django/django/blob/main/django/contrib/auth/models.py에 들어가봣는데
#     username을 찾아보니 username_validator = UnicodeUsernameValidator()를 쓴다
#     UnicodeUsernameValidator()를 따라 들어가보면
# class UnicodeUsernameValidator(validators.RegexValidator):
#     regex = r"^[\w.@+-]+\Z"
#     message = _(
#         "Enter a valid username. This value may contain only letters, "
#         "numbers, and @/./+/-/_ characters."
#     )
#     flags = 0
#     이런식으로 구현되어 있다.

urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, name='user_page'),
]
#   이렇게 되면 username이 post라면 위에서 걸러지게 되서 밑에까지 못오게 됨.
#   그러므로 model에 가서 username의 제한을 걸어줘야한다.