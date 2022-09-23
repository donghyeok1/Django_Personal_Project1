from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

# 위에처럼 쓰면 password 입력 받으면 암호화가 안됨.
# 장고 공식 깃허브에 들어가서 forms.py에 들어가 보면 잘 구현된 form이 있음!
# UserCreationForm을 import 해서 쓰도록 하자!
# https://github.com/django/django/blob/main/django/contrib/auth/forms.py


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 필수 기입란으로 설정해주는것
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta(UserCreationForm.Meta):
        # 만약 model = 우리 앱의 User로 설정 안해주면 auth.User로 인식해버림!
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        # 이메일 중복 금지
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email
