from django.contrib.auth.models import AbstractUser
from django.db import models

#  인스타그램 프로필
#  이름, 사용자 이름, 웹사이트, 소개, 이메일, 전화번호, 성별

# user 모델을 바꾸려고 하면 settings에 가서 database 다음으로
# AUTH_USER_MODEL = "auth.User" 설정해줘야함.
# accounts 라는 앱에 있는 user 모델을 현재 프로젝트에 대한 기본 장고 모델로 쓰겠다는 의미!
# user 모델 커스텀을 하기 위해서는 migrate 하기 전에 db 파일을 없애고 해야함!
# python manage.py makemigrations accounts 를 해주고 migrate 하면 됨.


class User(AbstractUser):
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)

