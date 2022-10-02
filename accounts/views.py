from django.contrib import messages
from django.contrib.auth import (
    get_user_model,
    login as auth_login)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import update_last_login
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import (
    LoginView, logout_then_login,
    PasswordChangeView as AuthPasswordChangeView)
from django.urls import reverse_lazy
import requests

# ,로 구분되는 단위는 튜플을 다 쓸 수 있다.
from accounts.forms import SignupForm, ProfileForm, PasswordChangeForm
from accounts.models import User

from mysite.settings.dev import KAKAO_REDIRECT_URI, KAKAO_API, KAKAO_REST_API_KEY

from io import BytesIO
import magic
import requests
from urllib.parse import urlparse
from django.core.files import File

def download(url):
    response = requests.get(url)
    binary_data = response.content
    temp_file = BytesIO()
    temp_file.write(binary_data)
    temp_file.seek(0)
    return temp_file

# 파일 확장자 추출
def get_buffer_ext(buffer):
    buffer.seek(0)
    mime_info = magic.from_buffer(buffer.read(), mime=True)
    buffer.seek(0)
    return mime_info.split('/')[-1]

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
            if User.objects.get(email=form.email):
                return
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
    return render(request, 'accounts/signup_form.html', {
        'form': form,
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
        'form': form,
    })


class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
    success_url = reverse_lazy("password_change")
    template_name = 'accounts/password_change_form.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "암호를 변경했습니다.")
        return super().form_valid(form)


# 깃허브에 들어가서 PasswordChangeView를 보면 기본 템플릿인 template_name이 정해져있다.
# 커스텀 해주도록 하자.
# 물론 success_url도 커스톰한다.
# form_valid를 커스텀하는데 super로 기본 form_valid를 호출하고 messages 기능만 넣어준다.
# 그런데 이전 암호와 바꿀 암호가 같아도 변경이 된다.
# form을 바꿔주도록 하자
# 커스텀한 form을 넣을 것이기 떄문에 form_class를 다시 정의해주자.

password_change = PasswordChangeView.as_view()


@login_required
def user_follow(request, username):
    follow_user = get_object_or_404(User, username=username, is_active=True)

    # request.user가 follow_user를 팔로우 할려고 합니다.
    request.user.following_set.add(follow_user)
    follow_user.follower_set.add(request.user)

    messages.success(request, f"{follow_user}님을 팔로우했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    # HTTP_REFERE이 있으면 가져오고 없으면 root를 가져오겠다.
    return redirect(redirect_url)


@login_required
def user_unfollow(request, username):
    unfollow_user = get_object_or_404(User, username=username, is_active=True)

    request.user.following_set.remove(unfollow_user)
    unfollow_user.follower_set.remove(request.user)

    messages.success(request, f"{unfollow_user}님을 언팔했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    # HTTP_REFERE이 있으면 가져오고 없으면 root를 가져오겠다.
    return redirect(redirect_url)

def kakao_login(request):
    client_id = KAKAO_REST_API_KEY
    redirect_uri = KAKAO_REDIRECT_URI
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=account_email"
    )

def kakao_callback(request):
    client_id = KAKAO_REST_API_KEY
    code = request.GET.get("code")

    redirect_uri = KAKAO_REDIRECT_URI
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
    )
    token_json = token_request.json()

    kakao_access_token = token_json.get("access_token")
    # refresh_token = token_json.get("refresh_token")

    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {kakao_access_token}"},
    )

    profile_json = profile_request.json()

    kakao_account = profile_json.get("kakao_account")

    email = kakao_account.get("email", None)

    first_name = kakao_account.get("profile").get("nickname")

    last_name = "_kakao"
    avatar = kakao_account.get("profile").get("thumbnail_image_url")

    temp_file = download(avatar)
    file_name = '{urlparse}.{ext}'.format(
        # url의 마지막 '/' 내용 중 확장자 제거
        # ex) url = 'https://~~~~~~/bag-1623898_960_720.jpg'
        #     -> 'bag-1623898_960_720.jpg'
        #     -> 'bag-1623898_960_720'
        urlparse=urlparse(avatar).path.split('/')[-1].split('.')[0],
        ext=get_buffer_ext(temp_file)
    )

    try:
        user = User.objects.get(email=email)
        if user.login_method == 'kakao':
            update_last_login(None, user)
            auth_login(request, user)

            redirect_url = request.META.get("HTTP_REFERER", "root")
            # HTTP_REFERE이 있으면 가져오고 없으면 root를 가져오겠다.
            return redirect(redirect_url)
    except get_user_model().DoesNotExist:
        user = get_user_model().objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            login_method='kakao',
            username=first_name,
        )
        user.avatar.save(file_name, File(temp_file))
        user.set_unusable_password()
        user.save()
        auth_login(request, user)
        update_last_login(None, user)

        redirect_url = request.META.get("HTTP_REFERER", "root")
        # HTTP_REFERE이 있으면 가져오고 없으면 root를 가져오겠다.
        return redirect(redirect_url)
    else:
        return JsonResponse({'message':'user already exist'})

