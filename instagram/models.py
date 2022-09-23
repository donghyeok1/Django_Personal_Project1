import re
from django.db import models
from django.conf import settings
from django.urls import reverse


# User를 끌고 올 때, from accounts.models import User로 해도 동작은 함.
# 하지만 from django.conf import settings를 import 하고
# settings.AUTH_USER_MODEL로 동작시키는 것이 조금 더 유연하게 코딩하는것.
# Post의 tag를 잘 구현하려면 django taggit이라는 라이브러리가 있음.
# django-taggit
# 그런데 우리는 공부를 위해 Tag라는 모델을 만들 것임.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="instagram/post/%Y/%m/%d")
    caption = models.CharField(max_length=500)
    tag_set = models.ManyToManyField('Tag', blank=True)
#     Tag라는 모델을 가져온다는 것. ManyToMany를 쓰는 이유는 여러 포스트가 있고 여러 태그가 존재하기 떄문
    location = models.CharField(max_length=100)

    # def get_absolute_url(self):
    #     return reverse()
    # get_absolute_url을 구현하려면 detailView도 구현해야함.

    def __str__(self):
        return self.caption

    def extract_tag_list(self):
        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.caption)
        # re.findall(r"#([a-zA-Z\dㄱ-힣]+)", post.caption)
        # 이렇게 쓰면 #뒤에 나오는 모든 알파벳들과 숫자, 한글까지 다 뽑아내겠다는 뜻

        tag_list = []
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
            # _ 여기는 created 같은 boolean 형태를 쓰는 것인데 _ 주면 있던 없던 리스트의 요소 한개를 반환
            # 전부다 반환 한 것은 tag_list 빈 리스트에 전부 집어넣기!
        return tag_list

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


