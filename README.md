# Django_Personal_Project1
https://donghyeokcoding.notion.site/bc555bb9511b4a81832b0af97b8fe153
## UserModel

**field**

- website_url
- bio
- phone_number
- gender
- avatar
- login_method

```python
follower_set = models.ManyToManyField("self", blank=True)

following_set = models.ManyToManyField("self", blank=True)

website_url = models.URLField(blank=True)

bio = models.TextField(blank=True)

phone_number = models.CharField(max_length=13, blank=True, validators=[
                                    RegexValidator(r"010-?[1-9]\d{3}-?\d{4}$")])

gender = models.CharField(max_length=1, blank=True,
                              choices=GenderChoices.choices)

avatar = models.ImageField(
        blank=True, upload_to="accounts/avatar/%Y/%m/%d")

login_method = models.CharField(
        max_length=6, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
```

- follower_set이나 following_set을 보면 다대다 필드로서 파라미터에 "self"를 넣어주면 유저간의 관계로 지정이 가능하다.

**function**

```python
@property
def name(self):
    return f"{self.first_name} {self.last_name}"
```

- 한국식 이름으로 표기하기 위함.

```python
@property
def avatar_url(self):
    if self.avatar:
        return self.avatar.url
    else:
        return resolve_url("pydenticon_image", self.username)
```

- 유저의 아바타가 없는 경우를 대비 하기 위해서 default로 pydenticon_image를 이용하여 유저 네임마다 각기 다른 랜덤 이미지를 생성.
- 근데 이건 사실 물음표 이미지를 써서 프로필 이미지를 설정하지 않은 유저들에게 똑같이 적용시키면 되기 떄문에 안 쓸것 같음.

```python
@property
def follower_count(self):
    return self.follower_set.count()

@property
def following_count(self):
    return self.following_set.count()
```

- 외래키 필드를 가지거나 ManyToMany, ManyToOne 처럼 소스 모델에 연결된 타겟 모델의 인스턴스들은 자신과 연결된 소스모델의 인스턴스들을 가져올 수 있는 Managet를 가지게 된다.
- 기본적으로 이 Manager는 FOO_set의 형태로 이름지어지며, 여기서 FOO는 소문자로 변환된 소스모델 이름(예를 들어, 소스 모델 이름이 Order라면, order_set)이다.
- Reverse accessor는 관계를 역참조할 수 있는 이 Manager를 가리킨다.
- 모델 필드명_set으로 지정이 되는데 만약 다른 이름을 쓰고 싶다면 파라미터 related_name을 바꿔주면 된다.
- 위에 코드는 Manage를 쓴 것이 아닌데 _set이라는 이름이 중복이 될 수 있기 때문에 만약 follower나 following이라는 필드명을 쓰려면 related_name을 재정의 해줘야 한다.

```python
like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_post_set", blank=True)
```

### QuerySet을 count()로 row를 세는 것과 len()으로 세는 것의 차이

- count()의 경우 SELECT COUNT(*) FROM 모델명 이 RDBS에서 실행되고 count가 python으로 전달될 것이다.
- len()의 경우 SELECT * FROM 모델명 을 한번 RDBS에서 실행하고 python으로 전달된 결과를 len()으로 셀 것이다.
- len()으로 count()를 대신하려하면 fetch를 하면서 시간이 O(N)이 걸리고 이 결과를 웹서버의 memory에 담으면서 storage에 O(N)이 발생하며 복사하는 시간이 걸려 time에도 O(N)이 추가로 발생한다. 거이에 추가적으로 len()이 돌아가는 시간도 발생한다.
- 결과적으로 count()가 len()보다 2배정도 빠르다.

## 회원가입 기능

### forms

```python
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

```

- UserCreationForm은 주어진 사용자의 이름과 비밀번호에서 권한 없이 사용자를 생성하는 양식이다.
- 유효성 검사를 다 해준다.
- __init__은 해당 함수를 실행시켰을 때 기본적으로 실행되는 함수이다.
    - 그래서 필수 기입란을 설정해주기 위해 fields의 required를 True로 바꾸어준다.
- 그리고 clean_email이라는 함수를 만들어서 유효성 검사를 한 후, 데이터베이스에 email이 있는지 체크해서 있다면 ValidationError를 호출하고 없다면 유효성 검사를 마친 email을 리턴해준다.

#### cleaned_data

- 말 그대로 깨끗한 데이터를 만드는 기능.
- 장고에서 FORM 인스턴스는 is_valid 함수를 가지고 있다.
    - 유효성 검사를 실시해주는 함수이다.
- 유효성 검사를 해서 참인 값들만 cleaned_data에 의해 딕셔너리 형태로 오브젝트에 담기게 된다.
- 만약 유효하지 않은 값들이 들어온다면?
    - 딕셔너리 형태로 출력을 하니, 키 값은 담기게 되고 벨류 값은 빈 값이 리턴된다.
    - 그래서 nickname이라는 객체가 유효하지 않은 값이 들어오게 되면, {'nickname': ''} 이런 식으로 빈 값을 출력해준다.



### views.py

```python
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if User.objects.get(email=form.email):
                return
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })
```

- 기본적인 통신 method는 GET이다. 
- 우리가 form을 작성하고 버튼을 누르면 POST 통신이기 때문에 POST일때 먼저 입력을 한다.
- 그리고 보통 form의 파라미터로 request.POST와 request.FILE을 준다. 
    - 무조건 순서가 POST 다음 FILE이다. 
    - 그런데 회원가입에서는 FILE을 받는 양식이 없기 때문에 POST만 주었다.
- form에서 clean과 model에서 validator를 쓴다. 
- clean이 필요할 때는
    - 특정 Form에서 1회성 유효성 검사 루틴이 필요할 때
    - 다수 필드값에 걸쳐서, 유효성 검사가 필요할 때
    - 필드 값을 변경할 필요가 있을 때
- 작성한 form이 유효하다면 email 중복 체크를 해줘야한다.
    - 하지만 우리는 form에서 중복체크를 했었다.
    - 애초에 form에서 이메일이 중복되는지 체크가 되면 raise로 에러를 발생시켜주기 때문에 if문 안으로 들어갈 수 없다. 하지만 나는 그냥 한번 더 해줬다.
    - save를 하게 되면 return 값으로 user를 넘겨주게 된다.
    - 그래서 우리는 유효성 검사를 통과하고 데이터베이스에 저장한 유저 오브젝트를 sigend_user로 저장시킨다.
- auth_login은 from django.contrib.auth import login as auth_login 이다.
    - __init__으로 가면 login이라는 함수가 있는데 이 함수를 auth_login으로 재정의 한것이다.
    - 백엔드 상에서 사용자가 로그인 되어 있게 설정을 해준다.
    - 회원가입을 하자마자 로그인을 하게 해주려고 login 함수를 이용하였다.
- 다음은 message이다. 성공 여부를 위해서 message 함수를 이용하였는데, 이렇게 쓰기만 해놓으면 홈페이지에 계속해서 쌓이게 된다.
    - 그래서 모든 페이지에 공통이 되는 layout.html에 메세지가 쌓이면 바로바로 뽑아낼 수 있게 구현하였다.

    ```html
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
    ```

- 마지막은 next_url이다. 
    - request.GET을 하게 되면 QueryDict를 리턴하게 해준다. 
    - 회원가입이 성공하고 나서 GET 요청을 이용해 next라는 인자를 뽑아내보면 default로 next_url이 설정이 되어 있는 경우가 있다. 만약 그런 경우 그 값을 next_url로 지정해주고 만약 없다면 "/"페이지로 이동하게 한다는 코드이다.

- 그리고 POST 통신이 아니고 GET 통신이면 우리는 비어있는 form 데이터를 보여줘야 하기 때문에 SignupForm을 호출해준다.
- render의 인자로 request를 주고 html을 주며 마지막으로 우리가 해당 html로 가지고 갈 오브젝트를 써준다. form 형식을 그대로 가져갈 것이기 때문에 "form": form 이라고 해주었다.

### templates

```html
{% extends "layout.html" %}
{% load bootstrap4 static %}
{% load bootstrap4 %}
{% block content %}
    <div class="container">
        <div class="row">
            <div class="col-sm-6 offset-sm-3">
                <div class="card">
                  <div class="card-header">회원가입</div>
                  <div class="card-body">
                    <form action="" method="POST" enctype="multipart/form-data">
                        {% csrf_token %}
                        {% bootstrap_form form %}
                        {% buttons %}
                              <button type="submit" class="btn btn-primary">
                                {{ submit_label|default:"회원가입" }}
                              </button>
                        {% endbuttons %}
                        <a href="{% url "accounts:signup-kakao" %}">
                            <img src="{% static "kakao_logo.png" %}" alt="kakao_login" />
                        </a>
                    </form>
                  </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```

- POST 통신일 하기 위해서 우리가 선언해 놓은 form 데이터를 가지고 와야한다. 우리는 form 이라는 tag로 설정을 해주었기 때문에 bootstrap_form을 이용하여 form을 보여준다.
- 보통 게시글 작성 폼이나 코멘트 작성 폼, 회원가입 폼, 로그인 폼, 등등 다 비슷해서 _form.html이라는 파일로 관리를 하였다.
- 하지만 소셜 로그인을 쓰면서 소셜 로그인 버튼을 추가하였기 때문에 쓰지 않았다.

```html
{% load bootstrap4 static %}
<div class="card">
  {% if form_title %}
  <div class="card-header">{{ form_title }}</div>
  {% endif %}
  <div class="card-body">
    {% if form %}
        <form action="" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            {% bootstrap_form form %}
            {% buttons %}
                  <button type="submit" class="btn btn-primary">
                    {{ submit_label|default:"Submit" }}
                  </button>
            {% endbuttons %}
        </form>
    {% else %}
        <div class="alert alert-danger">form 객체를 지정해주세요.</div>
    {% endif %}
  </div>
</div>
```

- 원래는 이렇게 _form.html 파일을 따로 만들어 놓고 include 해서 submit_label과 form_title만 따로 설정해주는 식으로 가져왔다.
- 버튼을 누르게 되면 POST 통신을 해서 위에서 선언해놓은 유효성 검사를 거치고 데이터베이스에 저장을 한 후, 설정해둔 url로 이동하게 된다.

### urls.py

```python
path('signup/', views.signup, name='signup'),
```

- 회원가입 url이다. 

## 로그인 기능

### views

```python
from django.contrib.auth.views import LoginView
```

- 장고에서 제공해주는 LoginView class를 사용하였다.

- template은 우리가 지정한 login_form.html으로 바꿔준다.

```python
login = LoginView.as_view(template_name="accounts/login_form.html")
```

### urls

```python
path('login/', views.login, name='login')
```

### templates

```html
{% extends "layout.html" %}
{% load bootstrap4 static %}
{% load bootstrap4 %}
{% block content %}
    <div class="container">
        <div class="row">
            <div class="col-sm-6 offset-sm-3">
                <div class="card">
                  <div class="card-header">로그인</div>
                  <div class="card-body">
                    <form action="" method="POST" enctype="multipart/form-data">
                        {% csrf_token %}
                        {% bootstrap_form form %}
                        {% buttons %}
                              <button type="submit" class="btn btn-primary">
                                {{ submit_label|default:"로그인" }}
                              </button>
                        {% endbuttons %}
                        <a href="{% url "accounts:signup-kakao" %}">
                            <img src="{% static "kakao_logo.png" %}" alt="kakao_login" />
                        </a>
                    </form>
                  </div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}
```

- form은 LoginView class에서 지정해주는 form_class인 AuthenticationForm을 사용하였다.
- 수행하고 난 후 다음 페이지로 이동하기 위한 url은 LoginView class의 resolove_url을 통해 이동된다.
    - 만약 next_page가 있다면 로그인 후 next_page로 이동
    - 없다면 루트 페이지인 "/"로 이동하게 된다.

## 로그아웃 기능

### views

```python
from django.contrib.auth.views from logout_then_login
```

장고에서 제공하는 logout_then_login 함수를 이용하였다.

```python
def logout(request):
    messages.success(request, "로그아웃되었습니다.")
    return logout_then_login(request)
```

- 위 프로젝트에서 사용한 logout 함수이다.

```python
def logout_then_login(request, login_url=None):
    """
    Log out the user if they are logged in. Then redirect to the login page.
    """
    login_url = resolve_url(login_url or settings.LOGIN_URL)
    return LogoutView.as_view(next_page=login_url)(request)
```

- 장고에서 제공해주는 logout_then_login 함수이다.
- logout 하고 나서 돌아갈 url을 설정해준 후 장고에서 제공해주는 LogoutView class를 리턴해준다.

```python
class LogoutView(RedirectURLMixin, TemplateView):
    """
    Log out the user and display the 'You are logged out' message.
    """

    # RemovedInDjango50Warning: when the deprecation ends, remove "get" and
    # "head" from http_method_names.
    http_method_names = ["get", "head", "post", "options"]
    template_name = "registration/logged_out.html"
    extra_context = None

    # RemovedInDjango50Warning: when the deprecation ends, move
    # @method_decorator(csrf_protect) from post() to dispatch().
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == "get":
            warnings.warn(
                "Log out via GET requests is deprecated and will be removed in Django "
                "5.0. Use POST requests for logging out.",
                RemovedInDjango50Warning,
            )
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        auth_logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)

    # RemovedInDjango50Warning.
    get = post

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            return resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                "site": current_site,
                "site_name": current_site.name,
                "title": _("Logged out"),
                "subtitle": None,
                **(self.extra_context or {}),
            }
        )
        return context
```

- logout을 하게 되면 장고에서 제공해주는 auth_logout 함수를 이용해 logout을 시켜준다.
    - auth_logout은 logout을 auth_logout으로 재정의해서 쓴것이다.

```python
def logout(request):
    """
    Remove the authenticated user's ID from the request and flush their session
    data.
    """
    # Dispatch the signal before the user is logged out so the receivers have a
    # chance to find out *who* logged out.
    user = getattr(request, "user", None)
    if not getattr(user, "is_authenticated", True):
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)
    request.session.flush()
    if hasattr(request, "user"):
        from django.contrib.auth.models import AnonymousUser

        request.user = AnonymousUser()
```

- 회원가입을 했을 때 썻던 login 함수랑 로직이 비슷하다. 
- logout은 template이 따로 필요없다.

## 프로필 수정 구현

### views

```python
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
```

- 프로필을 수정하기 위해서는 login이 되어 있는 상태여야 한다.
    - login_required를 이용해서 login이 되어있는지 체크해준다.
- 프로필 이미지 같은 FILE을 받을 수 있기 때문에 파라미터로 FILES를 써주는데, 주의해야 할 점은 첫번째 파라미터는 무조건 request.POST이고 두번째 파라미터는 request.FILES를 넣어주어야 한다.
- 현재 로그인이 되어 있는 user의 정보를 가져와야 하기 때문에 instance를 request.user로 설정해준다.
    - 그렇다면 ProfileForm에서 현재 user의 정보가 작성되어 있는 부분이 저장되어 있는 정보를 토대로 채워진다.
- form 유효성 검사를 해주고 저장을 시킨다.
    - redirect로 url에서 지정해준 이름 'profile_edit'을 이용한다.
        - 'accounts/edit/' 이다.
- else라면 POST 통신이 아닌 GET 통신이다.
    - 프로필 페이지로 이동을 했을 때 GET 통신으로 form을 불러와야 한다.
    - 일단 user의 정보를 토대로 form을 채워진 것을 보여줘야 하기 때문에 instance로 user를 준다.
- 그 후, render 함수를 이용해 profile_edit_form.html을 보여준다.
    - form 오브젝트를 form 이라는 이름으로 보내준다.    

### template

```html
{% extends "accounts/layout.html" %} 
{% load bootstrap4 %} 
{% block content %}
<div class="container">
  <div class="row">
    <div class="col-sm-6 offset-sm-3">
      {% include "_form.html" with form_title="프로필 수정" submit_label="프로필 수정" %}
    </div>
  </div>
</div>
{% endblock %}
```

- 이것이 profile_edit_form.html 이다.
- 미리 설정해 놓은 _form.html을 include해서 불러온다. 
    - form_title과 submit_label을 따로 설정해준다.
    - _form.html을 왜 미리 설정해두었냐면, 게시글 생성과 수정, 회원가입, 로그인 등등 다 같은 폼을 가지고 있어서 설정해둔것이다.
        - 하지만 회원가입과 로그인에서 카카오 소셜로그인이 추가되면서 회원가입 html과 로그인 html에서는 include 하지 않고 따로 다시 구현하였다.

```html
{% load bootstrap4 static %}
<div class="card">
  {% if form_title %}
  <div class="card-header">{{ form_title }}</div>
  {% endif %}
  <div class="card-body">
    {% if form %}
        <form action="" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            {% bootstrap_form form %}
            {% buttons %}
                  <button type="submit" class="btn btn-primary">
                    {{ submit_label|default:"Submit" }}
                  </button>
            {% endbuttons %}
        </form>
    {% else %}
        <div class="alert alert-danger">form 객체를 지정해주세요.</div>
    {% endif %}
  </div>
</div>
```

- form을 가져와서 보여준다.

### form

```python
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'website_url',
                  'bio', 'email', 'phone_number', 'gender', 'avatar'}
```

- profile 수정을 위해 프로필 form을 설정해준다.
- model을 User로 설정하고 fields들을 User 모델에서 설정했던 필드들을 가져온다.

### url

```python
path('edit/', views.profile_edit, name='profile_edit')
```

- 프로필 수정을 위한 url을 설정해준다.

## 비밀번호 변경 기능

### views

```python
from django.contrib.auth.views import PasswordChangeView as AuthPasswordChangeView
class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
    success_url = reverse_lazy("password_change")
    template_name = 'accounts/password_change_form.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "암호를 변경했습니다.")
        return super().form_valid(form)
```

- 장고에서 제공해주는 PasswordChangeView class를 AuthPasswordChangeView로 재정의한다.
- 재정의한 class를 상속받아서 안에 존재하는 field들을 custom 해준다.
    - success_url은 reverse를 이용해서 정의해주는데, 여기서 reverse_lazy로 재정의해준다.
    - 밑에서 설명하겠지만 import 할 때, python은 class를 evaluate 하기 때문이다.
- template과 form_class도 재정의 해준다.

    ```python
    class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """

    error_messages = {
        **SetPasswordForm.error_messages,
        "password_incorrect": _(
            "Your old password was entered incorrectly. Please enter it again."
        ),
    }
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )

    field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password
    ```


- PasswordChangeForm 안에서는 이전 비밀번호를 확인하고 유효성 검사를 해준다.

- SetPasswordForm을 상속받는다.

```python
class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages["password_mismatch"],
                    code="password_mismatch",
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
```

- new_password1과 new_password2를 유효성 검사해서 일치하는지, 패스워드 양식에 맞는지 체크해주고 return으로 password2를 준다.
- 하지만 이렇게 상속만 받고 SetPasswordForm을 custom 하지 않으면 예전 비밀번호와 바꿀 비밀번호가 같더라도 동작을 하게 된다.
    - 예외 조건을 걸기 위해서 form에서 custom 하도록 하자.


#### reverse

- Django의 reverse() 함수는 viewname과 args 및 kwargs를 인자로 받아 url string을 반환한다.

- 예컨대 news app에 다음과 같은 url이 등록되어 있다고 하자.

```python
from news import views

path('archive', views.archive, name='news-archive')
```

- 이 때 어떤 View 함수에서 위 url로 리다이렉트하고 싶다면 다음과 같이 사용한다.

```python
from django.urls import reverse

def myview(request):
    return HttpResponseRedirect(reverse('news:news-archive'))
```

- reverse()함수를 사용하면, url이 변경되더라도 View의 코드를 수정할 필요가 없다. 
- 일반적으로 url이 수정될 확률이 높은 점을 고려하면 합리적인 설계라 할 것이다.


##### reverse_lazy

- reverse_lazy는 reverse와 동일한 동작을 함수 호출시 곧바로 처리하지 않고, 나중에 해당 변수가 직접 접근되거나 메서드가 호출되었을 때 evaluate한다.

- reverse는 내부에서 urlconf를 참조하기 때문에 제대로 동작하기 위해서는 프로젝트의 urlconf가 모두 로드되어야 한다. 
    - 그러나 때에 따라 urlconf가 로드되기 전에 해당 값을 참조해야 할 수도 있다.

- 예컨대 아래의 경우 reverse로 success_url을 정의하면 동작하지 않는다.

```python
class JobCreateView(CreateView):
    template_name = 'company/job.html'
    form_class = JobForm
    success_url = reverse_lazy('job')
    # FIXME
    # success_url = reverse('job')
```

- 이는 Python은 모듈이 import될 때 class들을 evaluate하기 때문이다.

- 예시

```python
# test.py
def a():
	print('test1')

class B:
	print('test2')
```

```shell
>>> import test
>>> test2
```

- 따라서 이 경우 success_url을 reverse_lazy를 사용하여 정의하고, 나중에 필요할 때 reverse가 일어나도록 해야한다.

### form

```python
class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password2(self):
        old_password = self.cleaned_data.get("old_password")
        new_password2 = super().clean_new_password2()
        if old_password == new_password2:
            raise forms.ValidationError("새로운 암호를 입력해주세요.")
        return new_password2
```

- 현재 PasswordChangeForm을 상속을 받아서 class 안에 존재하는 clean_new_password2 함수를 재정의 해준다.
    - PasswordChangeForm에서는 cleaned_data["old_password"]로 입력받은 old_password를 가져올 수 있다.
    - clean_new_password2 함수는 PasswordChangeForm class가 SetPasswordForm을 상속받는다.
    - SetPAsswordForm에는 clean_new_password2 함수가 존재한다.
    - super().clean_new_password2를 이용해 return 값인 new_password2를 받아온다.
    - super()는 상속의 대상인 부모 클래스를 호출하는 함수이다.
    - PasswordChangeForm 클래스를 호출하는데 PasswordChangeForm은 SetPasswordForm을 상속 받고 있기 때문에 SetPasswordForm 함수를 호출할 수 있다.
- new_password1과 new_password2는 SetPasswordForm에서 같은지 유효성 검사를 해준다.
- new_password2를 리턴 받았따는것은 이 유효성 검사를 통과했다는 뜻.
- 그래서 예전 비밀번호와 바꾸고자 하는 비밀번호가 같은 경우면 에러를 출력해주도록 설정해준다. 

- django/views/generic/edit.py 로 들어가서 FormMixin class를 보면 form_valid 함수가 선언되어 있다.

```python
def form_valid(self, form):
    """If the form is valid, redirect to the supplied URL."""
    return HttpResponseRedirect(self.get_success_url())
```

- get_success_url로 redirect를 시켜준다.
- 그리고 messages를 이용하여 성공 메세지를 띄워준다.

### url

```python
path('password_change/', views.password_change, name='password_change')
```

- 이렇게 설정을 해준다.    
- 왜 class이름과 다른가?
    - view 단에서 password_change = PasswordChangeView.as_view() 로 정의를 해주었기 때문이다.

### template

```html
{% extends "accounts/layout.html" %} {% load bootstrap4 %} {% block content %}
<div class="container">
  <div class="row">
    <div class="col-sm-6 offset-sm-3">
      {% include "_form.html" with form_title="프로필 수정" submit_label="프로필 수정" %}
    </div>
  </div>
</div>
{% endblock %}
```

- 위에서 미리 만들어준 _form.html을 불러와서 form_title과 submit_label을 설정해준다.

## 팔로우 기능

### view

```python
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

    return redirect(redirect_url)
```

- url 상에서 username을 입력을 받는다.
- username과 일치하는 User를 불러온다.
     - 활성화된 계정만 불러온다.
- 해당 페이지에 들어간 user는 username을 가진 user에게 follow를 거는 것이기 때문에 following_set을 건드린다.
- 팔로우를 당한 사람은 follower_set을 건드려준다.
    - follow_user는 페이지에 로그인한 유저가 팔로우 하고 싶은 유저이다.
    - 그러므로 request.user는 로그인한 유저인데 그 유저의 following_set에 follow_user를 추가해준다.
    - follow_user의 입장에서는 follower가 늘어나는 것이기 때문에 follow_user.follower_set에 request.user를 더해준다.
- HTTP REFERER이 있으면 가져오고 없으면 root 페이지로 redirect_url을 설정해준다.
    - return으로 redirect 해준다.
- unfollow도 follow와 같은 로직이다.

## 카카오 소셜 로그인

### 사전 작업

- kakao developer 사이트에 가서 REST_API_KEY와 REDIRECT_URI를 설정해준다.
- settings에 따로 설정을 해주었다.
    - redirect_uri는 'http://127.0.0.1:8000/accounts/signup/kakao/callback/' 로 설정해줬다.
- 정보 제공에 필요한 정보들을 체크해준다.

### view

```python
def kakao_login(request):
    client_id = KAKAO_REST_API_KEY
    redirect_uri = KAKAO_REDIRECT_URI
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=account_email"
    )
```

- developer 사이트에 나와있는 가이드 대로 API_KEY와  REDIRECT_URI를 잘 활용해 login 페이지로 넘어가준다.
- 그렇게 되면 정보 동의 요청 사이트가 뜨게 된다. 수락을 하게 된다면
    - 우리가 설정해둔 redirect uri로 이동하게 된다.
    - 우리는 url 단에서 redirect uri와 같은 uri를 정의해두고 함수를 만든다.
- 위에 kakao_login 함수를 이용해 접근을 한 후, redirect uri 로 이동하게 되면 "code"를 받은 상태로 넘어가게 된다.

```python
def kakao_callback(request):
    client_id = KAKAO_REST_API_KEY
    code = request.GET.get("code")

    redirect_uri = KAKAO_REDIRECT_URI
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
    )
    token_json = token_request.json()

    kakao_access_token = token_json.get("access_token")

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
        urlparse=urlparse(avatar).path.split('/')[-1].split('.')[0],
        ext=get_buffer_ext(temp_file)
    )

    try:
        user = User.objects.get(email=email)
        if user.login_method == 'kakao':
            update_last_login(None, user)
            auth_login(request, user)
            results = {
                'id': user.id,
                'email': email,
            }
            redirect_url = request.META.get("HTTP_REFERER", "root")

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

        results = {
            'id': user.id,
            'email': email,
        }
        redirect_url = request.META.get("HTTP_REFERER", "root")

        return redirect(redirect_url)
    else:
        return JsonResponse({'message':'user already exist'})
```

- code를 request.GET.get("code")으로 불러온다.
- 그 code를 이용하여 

```python
"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
```

- 해당 사이트에서 token을 받아온다.
    - 받아온 token을 json()을 이용해 token_json이라는 변수로 저장해준다.
    - 그렇다면 token_json에는 access_token과 refresh_token이 있다.
    - access_token을 이용해 사용자의 프로필 정보를 불러올 것이기 때문에 따로 저장해준다.
        - refresh_token은 현 프로젝트에서 필요없다. 
    - 헤더에 accesS_token을 실어서 프로필 정보를 다 받아온다.
    - 필요한 정보들을 전부 빼온 후, 회원가입 혹은 로그인을 진행한다.
    - 만약 해당 이메일을 가진 유저가 존재하는 경우
        - 존재하는 유저가 카카오 계정으로 회원가입을 한 경우
            - 이미 해당 카카오 계정으로 회원가입을 한 유저이기 때문에 장고에서 제공해주는 login 함수를 이용하여 로그인을 해준다.
                - auth_login은 장고에서 제공해주는 login 함수를 우리가 편한데로 이름만 바꿔준 것이다.
        - 해당 이메일을 가진 유저가 존재하지 않는 경우
            - 해당 카카오 계정으로 회원가입을 진행해준다.
                - create 함수를 이용하여 각 필드들을 채워주고 데이터 베이스에 저장해준다.
                - 그 후, 장고에서 제공해주는 login 함수를 이용해 로그인 처리를 해준다.
        - 존재하는 유저가 카카오 계정이 아닌 경우
            - 이메일은 중복되면 안되는 것이기 때문에 이메일이 이미 존재한다는 에러 메세지를 띄워준다.

### template

```html
<a href="{% url "accounts:signup-kakao" %}">
    <img src="{% static "kakao_logo.png" %}" alt="kakao_login" />
</a>
```

- signup_form과 login_form html에 추가해준다.
- static 폴더에 있는 kakao_logo를 불러와주고 해당 이미지를 클릭하면 accounts 앱의 signup-kakao라는 name을 가진 url을 호출한다.
