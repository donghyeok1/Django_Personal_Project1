from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import gettext_lazy as _


#  인스타그램 프로필
#  이름, 사용자 이름, 웹사이트, 소개, 이메일, 전화번호, 성별

# user 모델을 바꾸려고 하면 settings에 가서 database 다음으로
# AUTH_USER_MODEL = "auth.User" 설정해줘야함.
# accounts 라는 앱에 있는 user 모델을 현재 프로젝트에 대한 기본 장고 모델로 쓰겠다는 의미!
# user 모델 커스텀을 하기 위해서는 migrate 하기 전에 db 파일을 없애고 해야함!
# python manage.py makemigrations accounts 를 해주고 migrate 하면 됨.


class User(AbstractUser):

    LOGIN_EMAIL = "email"
    LOGIN_NAVER = "naver"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, _("Email")),
        (LOGIN_NAVER, _("Naver")),
        (LOGIN_KAKAO, _("Kakao")),
    )

    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"
    follower_set = models.ManyToManyField("self", blank=True)
    # self로 지정하면 유저간의 관계로 지정가능
    following_set = models.ManyToManyField("self", blank=True)

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13, blank=True, validators=[
                                    RegexValidator(r"010-?[1-9]\d{3}-?\d{4}$")])
    gender = models.CharField(max_length=1, blank=True,
                              choices=GenderChoices.choices)
    avatar = models.ImageField(
        blank=True, upload_to="accounts/avatar/%Y/%m/%d")
    # 이렇게 이미지 파일을 지정해 놓으면 form을 보여주는 html에서 <form 안에 enctype="Multipart/form-data"
    # 되어있는지 확인하고, 받는 view 단에서 request.FILES와 같이 파일을 받는지 확인해야함
    # 그리고 pillow 설치 되어있는지 확인
    login_method = models.CharField(
        max_length=6, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    # 유저의 풀네임을 보여주기 위해서!

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)
    # 유저의 아바타가 없는 경우를 대비하기 위해서!

    @property
    def follower_count(self):
        return self.follower_set.count()

    @property
    def following_count(self):
        return self.following_set.count()
