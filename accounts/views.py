from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, logout_then_login
from accounts.forms import SignupForm, ProfileForm

login = LoginView.as_view(template_name="accounts/login_form.html")
# 로그인 ui를 바꾸고 싶다면 getbootsrap 페이지로 가서 documentation에 card 레이아웃을 찾아라

def logout(request):
    messages.success(request, "로그아웃되었습니다.")
    return logout_then_login(request)
# https://github.com/django/django/blob/main/django/contrib/auth/views.py
# logout_then_login 함수가 구현이 되어있음!
# logout을 한다면 바로 login 페이지로 보내버림!

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            # from django.contrib.auth import login as auth_login
            # github에 가보면 auth의 __init__.py에 login 함수가 있다.
            # login을 import 하는데 login은 겹칠 수 있으니 auth_login으로 이름을 바꾼다
            # 이 함수는 회원가입하자마자 로그인하게 해주는 함수이다.
            # 이걸 안쓰면 장고단에서 있는 user 모델을 바로 불러올 수 없다.
            messages.success(request, "회원가입 환영합니다.")
            # 이 메세지는 html에서 노출을 시키지 않으면 계속 쌓이게 됨.
            # layout.html에서 구현

            next_url = request.GET.get('next', '/')
            # GET 인자에서 next 인자를 가져와보고 없다면 /로 이동하겠다.

            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form' : form,
    })

# https://sendgrid.com/docs/for-developers/sending-email/django/
# 회원 가입 email 보내기 send_mail API(SMTP)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필을 수정/저장했습니다.")
            return redirect("profile_edit")
    #     프로필 수정을 했을때 POST 통신
    else:
        form = ProfileForm(instance=request.user)
    #     프로필을 불러올 때 GET 통신
    return render(request, "accounts/profile_edit_form.html", {
        'form' : form,
    })