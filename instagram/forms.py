from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'caption', 'location']
        widgets = {
            "caption": forms.Textarea
        }

# 왜 author와 tag_set이 fields에 없을까?
# 일단 tag_Set은 caption에서 뽑아낼것이기 떄문
# author는 글을 쓰는 유저가 로그인한 유저이기 떄문에 고를 수 있으면 안됨.
# 그래서 view단에서 POST 명령을 처리할 때, 따로 구현!
# 그리고 widgets를 써서 위처럼 쓰면 쓸 수 있는 상자 공간이 더 넓어짐.
# tag_set을 caption에서 뽑아낸다는것이 무슨 말일까?
# #이 들어간 문자를 쓰면 그건 태그!
