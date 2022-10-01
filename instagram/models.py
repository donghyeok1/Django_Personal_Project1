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

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
#         abstract를 True로 설정하면 db 테이블이 만들어지지 않는다!


class Post(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="my_post_set", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="instagram/post/%Y/%m/%d")
    caption = models.CharField(max_length=500)
    tag_set = models.ManyToManyField('Tag', blank=True)
#     Tag라는 모델을 가져온다는 것. ManyToMany를 쓰는 이유는 여러 포스트가 있고 여러 태그가 존재하기 떄문
    location = models.CharField(max_length=100)
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_post_set", blank=True)
    # manytomany 모델 정의하는 법 첫번째. 모델 안에 ManyToMany필드로 집어넣는다
    # 두번째는 직접 LikeUser라는 모델을 만들어서 post와 user를 외래키로 참조한다.
    # 세번째는 직접 정의한 모델을 Post 모델안에 ManytoMany 필드로 집어넣어준다!
    # 세번째를 쓰는 경우가 post와 user를 외래키로 참조를 받고 또 LikeUser 모델에 추가 필드를 구현하고 싶을 때 쓴다!.
    # 이렇게 쓰고 마이그레트를 하면 author의 related_name의 default가 post_set인데 둘이 약간 겹치게 됨.
    # 그럴때에는 author에 파라미터로 related_name을 my_post_set 이런식으로 변경해주자!
    # 여기서 related_name이란 리버스 네임인데
    # user에 대해서 Post.objects.filter(author=user)로 쓸 수 있는데
    # user.post_set.all() 이렇게도 접근 가능함.
    # 둘다 해당 user가 작성한 게시글들을 불러옴.
    # 원래 related_name은 해당 필드명_set 이런식으로 default로 생성이됨.
    # 이걸 이용하여 리버스 네임으로 접근해서 역 참조함
    # 그런데 이렇게 해서 오류가 났을 때 어느 한쪽의 related_name을 변경시켜준다기 보다는
    # 둘다 바꿔줌!
    # 그래서 user.my_post_set.all() 하면 user가 쓴 포스팅 목록을 뽑고
    # user.like_post_set.all() 하면 user가 좋아요 누른 포스팅 목록을 뽑아냄.

    def get_absolute_url(self):
        return reverse("instagram:post_detail", args=[self.pk])
    # get_absolute_url을 구현하려면 detailView도 구현해야함.
    # return reverse("instagram:post_detail", kwargs={"pk": self.pk}) 이렇게 써도 됨

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

    def is_like_user(self, user):
        #         좋아요를 눌렀을때와 안눌렀을떄의 하트를 다르게 하기 위함!
        return self.like_user_set.filter(pk=user.pk).exists()

    class Meta:
        ordering = ['-id']


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Comment(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        ordering = ['-id']
