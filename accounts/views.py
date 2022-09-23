from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.forms import SignupForm


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
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