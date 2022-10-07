# 기능 설명(구현 코드)

# layout

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>Instagram with donghyeok</title>

<link rel="stylesheet"href="{% static 'bootstrap-5.2.1-dist/css/bootstrap.min.css' %}" />
<script src="//kit.fontawesome.com/f77c68182f.js"crossorigin="anonymous"></script>

<script src="{% static 'jquery-3.6.1.min.js' %}"></script>
<script src="{% static "jquery.form.js" %}"></script>
<script src="{% static 'bootstrap-5.2.1-dist/js/bootstrap.min.js' %}"></script>

</head>
<body>

{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
    {% endfor %}
{% endif %}
    <div class="border-bottom mb-3">
        <div class="container">
            <div class="row">
                <div class="col-sm-12">
                    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 bg-white">
                        <h5 class="my-0 mr-md-auto font-weight-normal">
                            <svg class="mr-3"fill="#262626"height="24"viewBox="0 0 48 48"width="24"><path d="M13.86.13A17 17 0 008 1.26 11 11 0 003.8 4 12.22 12.22 0 001 8.28 18 18 0 00-.11 14.1c-.13 2.55-.13 3.38-.13 9.9s0 7.32.13 9.9A18 18 0 001 39.72 11.43 11.43 0 003.8 44 12.17 12.17 0 008 46.74a17.75 17.75 0 005.82 1.13c2.55.13 3.38.13 9.9.13s7.32 0 9.9-.13a17.82 17.82 0 005.83-1.13A11.4 11.4 0 0043.72 44a11.94 11.94 0 002.78-4.24 17.7 17.7 0 001.13-5.82c.13-2.55.13-3.38.13-9.9s0-7.32-.13-9.9a17 17 0 00-1.13-5.86A11.31 11.31 0 0043.72 4a12.13 12.13 0 00-4.23-2.78A17.82 17.82 0 0033.66.13C31.11 0 30.28 0 23.76 0s-7.31 0-9.9.13m.2 43.37a13.17 13.17 0 01-4.47-.83 7.25 7.25 0 01-2.74-1.79 7.25 7.25 0 01-1.79-2.74 13.23 13.23 0 01-.83-4.47c-.1-2.52-.13-3.28-.13-9.7s0-7.15.13-9.7a12.78 12.78 0 01.83-4.44 7.37 7.37 0 011.79-2.75A7.35 7.35 0 019.59 5.3a13.17 13.17 0 014.47-.83c2.52-.1 3.28-.13 9.7-.13s7.15 0 9.7.13a12.78 12.78 0 014.44.83 7.82 7.82 0 014.53 4.53 13.12 13.12 0 01.83 4.44c.13 2.51.13 3.27.13 9.7s0 7.15-.13 9.7a13.23 13.23 0 01-.83 4.47 7.9 7.9 0 01-4.53 4.53 13 13 0 01-4.44.83c-2.51.1-3.28.13-9.7.13s-7.15 0-9.7-.13m19.63-32.34a2.88 2.88 0 102.88-2.88 2.89 2.89 0 00-2.88 2.88M11.45 24a12.32 12.32 0 1012.31-12.35A12.33 12.33 0 0011.45 24m4.33 0a8 8 0 118 8 8 8 0 01-8-8"></path></svg>
                            <a href="{% url "root" %}">
                              <img src="{% static "logo.png" %}"alt="Instagram" />
                            </a>
                        </h5>
                        <nav class="d-inline-flex mt-2 mt-md-0 ms-md-auto">
                        <a class="me-3 py-2 text-dark text-decoration-none"href="/">
                            <svg aria-label="홈"class="_ab6-"color="#262626"fill="#262626"height="24"role="img"viewBox="0 0 24 24"width="24"><path d="M22 23h-6.001a1 1 0 01-1-1v-5.455a2.997 2.997 0 10-5.993 0V22a1 1 0 01-1 1H2a1 1 0 01-1-1V11.543a1.002 1.002 0 01.31-.724l10-9.543a1.001 1.001 0 011.38 0l10 9.543a1.002 1.002 0 01.31.724V22a1 1 0 01-1 1z"></path></svg>
                        </a>
                        <a class="me-3 py-2 text-dark text-decoration-none"href="/direct/inbox/">
                            <svg aria-label="Direct"class="_ab6-"color="#262626"fill="#262626"height="24"role="img"viewBox="0 0 24 24"width="24"><line fill="none"stroke="currentColor"stroke-linejoin="round"stroke-width="2"x1="22"x2="9.218"y1="3"y2="10.083"></line><polygon fill="none"points="11.698 20.334 22 3.001 2 3.001 9.218 10.084 11.698 20.334"stroke="currentColor"stroke-linejoin="round"stroke-width="2"></polygon></svg>
                        </a>
                        <a class="me-3 py-2 text-dark text-decoration-none"href="/post/new/">
                            <svg aria-label="새로운 게시물"class="_ab6-"color="#262626"fill="#262626"height="24"role="img"viewBox="0 0 24 24"width="24"><path d="M2 12v3.45c0 2.849.698 4.005 1.606 4.944.94.909 2.098 1.608 4.946 1.608h6.896c2.848 0 4.006-.7 4.946-1.608C21.302 19.455 22 18.3 22 15.45V8.552c0-2.849-.698-4.006-1.606-4.945C19.454 2.7 18.296 2 15.448 2H8.552c-2.848 0-4.006.699-4.946 1.607C2.698 4.547 2 5.703 2 8.552z"fill="none"stroke="currentColor"stroke-linecap="round"stroke-linejoin="round"stroke-width="2"></path><line fill="none"stroke="currentColor"stroke-linecap="round"stroke-linejoin="round"stroke-width="2"x1="6.545"x2="17.455"y1="12.001"y2="12.001"></line><line fill="none"stroke="currentColor"stroke-linecap="round"stroke-linejoin="round"stroke-width="2"x1="12.003"x2="12.003"y1="6.545"y2="17.455"></line></svg>
                        </a>
                        <a class="me-3 py-2 text-dark text-decoration-none"href="/explore/">
                            <svg aria-label="사람 찾기"class="_ab6-"color="#262626"fill="#262626"height="24"role="img"viewBox="0 0 24 24"width="24"><polygon fill="none"points="13.941 13.953 7.581 16.424 10.06 10.056 16.42 7.585 13.941 13.953"stroke="currentColor"stroke-linecap="round"stroke-linejoin="round"stroke-width="2"></polygon><polygon fill-rule="evenodd"points="10.06 10.056 13.949 13.945 7.581 16.424 10.06 10.056"></polygon><circle cx="12.001"cy="12.005"fill="none"r="10.5"stroke="currentColor"stroke-linecap="round"stroke-linejoin="round"stroke-width="2"></circle></svg>
                        </a>
                        <a class="me-3 py-2 text-dark text-decoration-none"href="/accounts/activity/">
                            <svg aria-label="활동 피드"class="_ab6-"color="#262626"fill="#262626"height="24"role="img"viewBox="0 0 24 24"width="24"><path d="M16.792 3.904A4.989 4.989 0 0121.5 9.122c0 3.072-2.652 4.959-5.197 7.222-2.512 2.243-3.865 3.469-4.303 3.752-.477-.309-2.143-1.823-4.303-3.752C5.141 14.072 2.5 12.167 2.5 9.122a4.989 4.989 0 014.708-5.218 4.21 4.21 0 013.675 1.941c.84 1.175.98 1.763 1.12 1.763s.278-.588 1.11-1.766a4.17 4.17 0 013.679-1.938m0-2a6.04 6.04 0 00-4.797 2.127 6.052 6.052 0 00-4.787-2.127A6.985 6.985 0 00.5 9.122c0 3.61 2.55 5.827 5.015 7.97.283.246.569.494.853.747l1.027.918a44.998 44.998 0 003.518 3.018 2 2 0 002.174 0 45.263 45.263 0 003.626-3.115l.922-.824c.293-.26.59-.519.885-.774 2.334-2.025 4.98-4.32 4.98-7.94a6.985 6.985 0 00-6.708-7.218z"></path></svg>
                        </a>
                        <a class="me-3 py-2 text-dark text-decoration-none"href="{% url "accounts:profile_edit" %}">
                            <img src="{{ user.avatar_url }}"class="rounded-circle"style="width: 24px; height: 24px;" />
                        </a>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {% block content %}
    {% endblock %}
    <div class="border-top mt-3">
        <div class="container">
            <footer class="pt-4 my-md-5 pt-md-5">
                <div class="row">
                <div class="col-12 col-md">
                    <img class="mb-2"src="{% static "admin.jpg" %}"alt=""width="24"height="19">
                    <small class="d-block mb-3 text-muted">© 2022</small>
                </div>
                <div class="col-6 col-md">
                    <h5>Features</h5>
                    <ul class="list-unstyled text-small">
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Cool stuff</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Random feature</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Team feature</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Stuff for developers</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Another one</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Last time</a></li>
                    </ul>
                </div>
                <div class="col-6 col-md">
                    <h5>Resources</h5>
                    <u lclass="list-unstyled text-small">
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Resource</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Resource name</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Another resource</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Final resource</a></li>
                    </ul>
                </div>
                <div class="col-6 col-md">
                    <h5>About</h5>
                    <ul class="list-unstyled text-small">
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Team</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Locations</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Privacy</a></li>
                    <li class="mb-1"><a class="link-secondary text-decoration-none"href="#">Terms</a></li>
                    </ul>
                </div>
                </div>
            </footer>
        </div>
    </div>
</body>
</html>
```

- 인스타그램의 대문 페이지를 F12 버튼을 누르고 들어가서 참조했다.
- 그곳에서 추가된 기능은 jquery 추가, 부트스트랩 추가, 메세지 기능 추가, 그리고 부트스트랩 홈페이지에서 바닥 페이지와 헤더쪽을 가져왔다.
    - layout은 모든 페이지에 공통되는 html이다.
    - 그래서 view 단에서 발생한 메세지들이 쌓여있는데 이것을 공통되는 layout에서 분출을 해준다.
    - 메세지는 messages라는 변수로 바로 접근이 가능하다.
    - 인스타그램에서 가져온 각 아이콘에 반응해야할 주소를 써준다.

# accounts app

## 유저 모델

- **field**
    
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
    
- **function**
    
    ```python
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"ve_url("pydenticon_image", self.username)
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
    
    - **QuerySet을 count()로 row를 세는 것과 len()으로 세는 것의 차이**
        - count()의 경우 SELECT COUNT(*) FROM 모델명 이 RDBS에서 실행되고 count가 python으로 전달될 것이다.
        - len()의 경우 SELECT * FROM 모델명 을 한번 RDBS에서 실행하고 python으로 전달된 결과를 len()으로 셀 것이다.
        - len()으로 count()를 대신하려하면 fetch를 하면서 시간이 O(N)이 걸리고 이 결과를 웹서버의 memory에 담으면서 storage에 O(N)이 발생하며 복사하는 시간이 걸려 time에도 O(N)이 추가로 발생한다. 거이에 추가적으로 len()이 돌아가는 시간도 발생한다.
        - 결과적으로 count()가 len()보다 2배정도 빠르다.

## 회원가입 기능

- **form**
    
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
    - **cleaned_data**
        - 말 그대로 깨끗한 데이터를 만드는 기능.
        - 장고에서 FORM 인스턴스는 is_valid 함수를 가지고 있다.
            - 유효성 검사를 실시해주는 함수이다.
        - 유효성 검사를 해서 참인 값들만 cleaned_data에 의해 딕셔너리 형태로 오브젝트에 담기게 된다.
        - 만약 유효하지 않은 값들이 들어온다면?
            - 딕셔너리 형태로 출력을 하니, 키 값은 담기게 되고 벨류 값은 빈 값이 리턴된다.
            - 그래서 nickname이라는 객체가 유효하지 않은 값이 들어오게 되면, {'nickname': ''} 이런 식으로 빈 값을 출력해준다.
- **view**
    
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
        - 다수 필드값에 걸쳐서, 유효성 검사가 필요할
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
- **template**
    
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
- **url**
    
    ```python
    path('signup/', views.signup, name='signup')
    ```
    
    - 회원가입 url이다.

## **로그인 기능**

- **view**
    
    ```python
    from django.contrib.auth.views import LoginView
    
    login = LoginView.as_view(template_name="accounts/login_form.html")
    ```
    
    - 장고에서 제공해주는 LoginView class를 사용하였다.
    - template은 우리가 지정한 login_form.html으로 바꿔준다.
- **template**
    
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
- **url**
    
    ```python
    path('login/', views.login, name='login')
    ```
    

## 로그아웃 기능

- **view**
    
    ```python
    from django.contrib.auth.views from logout_then_login
    ```
    
    - 장고에서 제공하는 logout_then_login 함수를 이용하였다.
    
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
- **url**
    
    ```python
    path('logout/', views.logout, *name*='logout')
    ```
    

## 프로필 수정 구현

- **form**
    
    ```python
    class ProfileForm(forms.ModelForm):
        class Meta:
            model = User
            fields = {'first_name', 'last_name', 'website_url',
                      'bio', 'email', 'phone_number', 'gender', 'avatar'}
    ```
    
    - profile 수정을 위해 프로필 form을 설정해준다.
    - model을 User로 설정하고 fields들을 User 모델에서 설정했던 필드들을 가져온다.
- **view**
    
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
- **template**
    
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
    
    - from을 가져와서 보여준다.
- **url**
    
    ```python
    path('edit/', views.profile_edit, name='profile_edit')
    ```
    
    - 프로필 수정을 위한 url을 설정해준다.

## 비밀번호 변경 기능

- **view**
    
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
    - **reverse**
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
    - **reverse_lazy**
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
            
            ```bash
            >>> import test
            >>> test2
            ```
            
        - 따라서 이 경우 success_url을 reverse_lazy를 사용하여 정의하고, 나중에 필요할 때 reverse가 일어나도록 해야한다.
    
- **form**
    
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
- **template**
    
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
    
    - 위에서 미리 만들어준 *form.html을 불러와서 form_title과 submit_label을 설정해준다.*
- **url**
    
    ```python
    path('password_change/', views.password_change, name='password_change')
    ```
    
    - 이렇게 설정을 해준다.
    - 왜 class이름과 다른가?
        - view 단에서 password_change = PasswordChangeView.as_view() 로 정의를 해주었기 때문이다.

## 팔로우 기능

- **view**
    
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
- **url**
    
    ```python
    re_path(r'^(?P<username>[\w.@+-]+)/follow/$',
            views.user_follow,name='user_follow'),
    re_path(r'^(?P<username>[\w.@+-]+)/unfollow/$',
            views.user_unfollow,name='user_unfollow'),
    ```
    
    - 여기서 나오는 username은 팔로우를 당하는 user의 username이다.
    - view단에서 username을 pk로 받는데 이 username을 넘겨주는 것이다.

## 카카오 소셜 로그인

### 사전 작업

- kakao developer 사이트에 가서 REST_API_KEY와 REDIRECT_URI를 설정해준다.
- settings에 따로 설정을 해주었다.
    - redirect_uri는 'http://127.0.0.1:8000/accounts/signup/kakao/callback/' 로 설정해줬다.
- 정보 제공에 필요한 정보들을 체크해준다.
- **view**
    
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
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
    )
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
- **template**
    
    ```html
    <a href="{% url "accounts:signup-kakao" %}">
        <img src="{% static "kakao_logo.png" %}" alt="kakao_login" />
    </a>
    ```
    
    - signup_form과 login_form html에 추가해준다.
    - static 폴더에 있는 kakao_logo를 불러와주고 해당 이미지를 클릭하면 accounts 앱의 signup-kakao라는 name을 가진 url을 호출한다.
- **url**
    
    ```python
    path('signup/kakao/', views.kakao_login,name='signup-kakao'),
    path('signup/kakao/callback/', views.kakao_callback,name='signup-kakao-callback'),
    ```
    
    - callback 함수를 호출하는 url은 무조건 카카오 디벨로퍼 사이트에 설정한 redirect url과 같게 해야한다!

# instagram app

## 메인 화면 기능

- **view**
    
    ```python
    @login_required
    def index(request):
    		post_list = Post.objects\
            .filter(
                Q(author=request.user)
                |
                Q(author__in=request.user.following_set.all())
            )
    		suggested_user_list = get_user_model().objects.all().exclude(
    pk=request.user.pk).exclude(pk__in=request.user.following_set.all())[:3]
    
    		comment_form = CommentForm()
        return render(request, "instagram/index.html", {
            "suggested_user_list": suggested_user_list,
            "post_list": post_list,
            "comment_form": comment_form,
        })
    ```
    
    - post_list
        - Q 객체를 이용해서 or 메소드를 이용할 수 있다.
            - 자신이 쓴 게시글이거나
            - 팔로잉 목록에 있는 유저들이 쓴 게시글
            - 전부를 메인 화면에 띄워주는 것이다.
            - 이렇게 하면 post_list 오브젝트에 자신이 쓰거나 팔로우를 한 유저들의 게시글들의 쿼리셋이 저장이 된다.
    - suggested_user_list
        - 팔로우를 하지 않은 유저들 중 가입한 날을 기준으로 3명을 추천 친구로 보여주기 위한 list이다.
        - exclude 함수는 filtering의 반대임.
            - 필터링은 특정 정보를 가진 유저를 가져오는 것이라면 exclude는 특정 정보를 가진 유저를 제외한 유저들을 불러오겠다는 의미
            - 로그인한 user와 그 user의 following 목록에 있는 유저들을 제외하고 3명까지 유저 목록을 seggested_user_list에 저장을 한다.
    - comment_form
        - CommentForm()을 comment_form 오브젝트로 받아서 template으로 전달해주는 것
        - CommentForm은 코멘트 작성 기능에서 설명할 것임.
- **template**
    
    ```html
    {% extends "instagram/layout.html" %}
    {% block content %}
        <div class="container">
          <div class="row">
            <div class="col-sm-12">
              <a href="{% url 'instagram:post_new' %}"class="btn btn-primary">
                새 포스팅 쓰기
              </a>
            </div>
          </div>
          <div class="row">
            <div class="col-sm-8">
              <hr />
              {% for post in post_list %}
                <div class="mb-3">
                    {% include "instagram/_post_card.html" %}
                </div>
              {% empty %}
                  포스팅이 없습니다.
              {% endfor %}
            </div>
            <div class="col-sm-4">{% include "instagram/timeline_sidebar.html" %}</div>
          </div>
        </div>
    {% endblock %}
    ```
    
    - view단에서 선언한 index 함수에서 우리는
        - post_list
        - suggested_user_list
        - comment_form
    - 이 세가지 오브젝트를 template으로 넘겨주었다.
    - 게시글 하나를 감싸는 _post_card.html을 따로 include
    - 사이드 바에 추천친구를 보여주는 timeline_sidebar.html을 따로 include
- **url**
    
    ```python
    # instagram/urls.py
    path('', views.index, *name*='index')
    ```
    
    ```python
    # mysite/urls.py
    path('', RedirectView.as_view(*pattern_name*='instagram:index'), *name*='root')
    ```
    
    - RedirectView는 [장고 공식문서](https://github.com/django/django/blob/da02cbd1effc951b14c981925d0e26a39566649e/django/views/generic/base.py#L229)에 존재하는 class를 가져온 것이다.
        - pattern_name을 정해주면 reverse 함수를 이용해 pattern_name에 해당하는 url로 이동해준다.
        - 그렇다면 mysite는 제일 최상위 project 이름인데, 기본 root 페이지를 instagram앱의 index 이름을 가진 url로 정하겠다는 의미이다.
        - 그리고 index라는 이름을 가진 url은 view단에서 index 함수를 호출한다.
        
    - 그래서 가장 루트 페이지로 이동을 하게 되면 로그인 한 유저의 팔로잉 유저들의 게시글과 자신의 게시글, 팔로잉을 하지 않은 유저들의 목록을 3명까지 보여주게 된다.

## 포스트 모델

- **field**
    
    ```python
    author = models.ForeignKey(
          settings.AUTH_USER_MODEL,related_name="my_post_set",on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="instagram/post/%Y/%m/%d")
    caption = models.CharField(max_length=500)
    tag_set = models.ManyToManyField('Tag',blank=True) 
    location = models.CharField(max_length=100)
    like_user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,related_name="like_post_set",blank=True)
    ```
    
- **function**
    
    ```python
    def get_absolute_url(self):
        return reverse("instagram:post_detail",args=[self.pk])
    
    def __str__(self):
        returnself.caption
    
    def extract_tag_list(self):
        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)",self.caption)
    		
    		tag_list = []
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
    		return tag_lis
    def is_like_user(self,user):
    		return self.like_user_set.filter(pk=user.pk).exists()
    
    class Meta:
        ordering = ['-id']
    ```
    
    - get_absolute_url을 선언해 놓으면 이 함수를 이용해 해당 url에 접근 가능하다.
    - extract_tag_list는 포스팅 기능 측에서 설명을 하도록 하겠다.
    - is_like_user도 게시글 좋아요 기능 측에서 설명을 하도록 하겠다.
- **BaseModel**
    
    ```python
    class BaseModel(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        class Meta:
            abstract = True
    
    class Post(BaseModel):
    	...
    	...
    ```
    
    - created_at과 updated_at은 모든 모델에서 적용하는 필드이다.
    - 계속 쓰기 귀찮으니 따로 BaseModel이라는 class를 선언해서 필요한 모델에 상속해주면 된다.
    - 그리고 abstract = True로 만들어주면 db 테이블이 따로 만들어지지 않는다.
        - 하지만 불러올 수는 있다!

## 태그 모델

- **field**
    
    ```python
    name = models.CharField(*max_length*=50, *unique*=True)
    ```
    
- **function**
    
    ```python
    def __str__(self):
        return self.name
    ```
    

## 포스팅 기능

- **view**
    
    ```python
    @login_required
    def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
    						post.author = request.user
                post.save()
                post.tag_set.add(*post.extract_tag_list())
    						messages.success(request, "포스팅을 저장했습니다.")
                return redirect(post)
    		else:
            form = PostForm()
    
        return render(request, "instagram/post_form.html", {
            "form": form,
        })
    ```
    
    - 포스팅을 하는 기능에는 포스트 폼을 불러오기 위한 GET과 사용자가 입력한 폼을 받아오는 POST가 있다.
        - POST
            - 위에서 말했듯이 from의 파라미터는 무조건 POST가 먼저고 두번째로 FILES를 설정 해줘야 한다.
            - 사용자에게 입력 받은 form 유효성 검사
                - 유효성 검사를 합격했다면 입력 받은 form을 save 해주고 post 오브젝트에 저장해준다.
                - commit = True이면 필수 필드인 author 없이 인스턴스를 저장하기 때문에 오류가 발생한다.
                - 하지만 post를 작성할 때 유저는 이미 login_required를 통과한 유저이기 때문에 자동으로 저장이 되게끔 설정 해줘야 한다.
                - 그렇기 때문에 commit = False로 해주고 현재 사용자의 정보를 post.author에 넣어준다.
                - Post 모델에서 선언해준 extract_tag_list를 불러준다.
                    
                    ```python
                    def extract_tag_list(self):
                        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)",self.caption)
                    tag_list = []
                        for tag_name in tag_name_list:
                            tag, _ = Tag.objects.get_or_create(name=tag_name)
                            tag_list.append(tag)
                    return tag_list
                    ```
                    
                    - re.findall 함수는 위에 형식대로 쓴다면 caption에 쓰여져 있는 # 뒤에 문자들 혹은 숫자들 전부를 tag_name_list 에 집어넣어준다.
                    - 그래서 for 문을 돌려보며 하나씩 뽑아보는데, 해당 tag_name이 Tag 모델에 존재 한다면 저장하지 않고 만약 존재하지 않는다면 tag 변수에 저장을 한 후, tag_list에 추가해준다.
                    - 그리고 tag_list를 return 해준다.
                    - 그렇게 되면 # 뒤에 문자를 tag로 인식해 해당 post의 caption 안에 어떤 태그가 있는지 반환해준다.
                - 해당 post의 caption에서 tag_list를 전부 뽑은 다음 post의 ManyToMany 필드인 tag_set에 add 해준다.
                    - ManytoMany field에서는 add명령어를 통해 한개씩 넘길 수 있는데 넘기는 인자가 리스트니깐 *로 한번에 좌르륵 넘기기~
                    - save를 한 후에 add를 해야 한다.
                - redirect(post)
                    - redirect의 인자로 post 오브젝트를 주기 위해서는 post 오브젝트에 저장된 Post 모델에 get_absolute_url 함수가 정의되어 있어야 한다.
                    
                    ```python
                    def get_absolute_url(self):
                        return reverse("instagram:post_detail",args=[self.pk])
                    ```
                    
                    - 이렇게 정의를 한 후, redirect 인자로 post를 주게 되면 get_absolute_url 함수를 호출해서 해당 포스트의 상세 페이지로 이동하게 해준다.
                    - post_detail 쪽은 포스트 detail 쪽으로 가서 설명을 하겠다.
        - GET
            - 우리가 작성한 PostForm 형태를 불러오기만 하면 되기 때문에 어떠한 form을 불러올지만 정해주면 된다.
- **form**
    
    ```python
    class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['photo', 'caption', 'location']
            widgets = {
                "caption": forms.Textarea,
            }
    ```
    
    - 왜 author와 tag_set이 fields에 없을까?
        - 일단 tag_set은 caption에서 뽑아낼 것이기 때문이다.
        - author는 글을 쓰는 유저가 로그인한 유저이기 때문에 고를 수 있으면 안된다.
        - 그래서 view단에서 따로 구현한 것이다.
    - widgets은 caption은 쓸 수 있는 상자 공간이 더 넓어진다.
- **template**
    
    ```html
    {% extends "instagram/layout.html" %} {% load bootstrap4 %} {% block content %}
    <div class="container">
      <div class="row">
        <div class="col-sm-6 offset-sm-3">
          {% include "_form.html" with form_title="새 포스팅 쓰기" submit_label="새 포스팅 쓰기" %}
        </div>
      </div>
    </div>
    {% endblock %}
    
    ```
    
    - 맨 앞에서 _form.html을 구현해 놓았다.
    - form_title과 submit_label만 따로 설정해주고 include를 통해 가져오면 된다.
- **url**
    
    ```python
    path('post/new/', views.post_new, *name*='post_new')
    ```
    

## 상세 페이지 기능

- **view**
    
    ```python
    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentForm()
    		return render(request, "instagram/post_detail.html", {
            "post": post,
            "comment_form": comment_form,
        })
    ```
    
    - url에서 받아온 pk로 Post 모델의 특정 Post를 불러온다.
    - 포스트 상세 페이지에서도 댓글 폼이 보여야 하기 때문에 comment_form도 불러온다.
- **template**
    
    ```html
    {% extends "instagram/layout.html" %}
    {% load thumbnail humanize instagram_tags bootstrap4 %}
    {% block content %}
        <div class="container">
            <div class="row">
                <div class="col-sm-6 offset-sm-3">
                    <div class="card">
                        <div class="card-header">
                            <img src="{{ post.author.avatar_url }}"style="width: 32px; height: 32px;"/>
                            <a href="{% url "instagram:user_page" post.author.username %}">
                                {{ post.author.name }}
                            </a>
                        </div>
                        <div class="card-body">
                            <img src="{{ post.photo.url }}"style="width: 512px; height: 512px;"/>
                            <div>
                                {% if post|is_like_user:user %}
                                    <a href="{% url "instagram:post_unlike" post.pk %}"style="color: inherit;">
                                        <i class="fa-solid fa-heart"></i>
    </a>
                                {% else %}
                                    <a href="{% url "instagram:post_like" post.pk %}"style="color: inherit;">
                                        <i class="fa-regular fa-heart"></i>
                                    </a>
                                {% endif %}
                            </div>
                            <div id= "post-detail-{{ post.pk }}-comment-list"class="comment-list mt-3 mb-3">
                                    {% for comment in post.comment_set.all %}
                                        {% include "instagram/_comment.html" %}
                                    {% endfor %}
                            </div>
                            <div>
                                {% for tag in post.tag_set.all %}
                                    <span class="badge text-bg-primary">#{{ tag.name }}</span>
                                {% endfor %}
                            </div>
                            <div>
                                    <small>
                                        {{ post.created_at|naturaltime }}
                                    </small>
                            </div>
    										</div>
                        <div class="card-footer">
                            <form id="post-detail-{{ post.pk }}-comment-form"action="{% url "instagram:comment_new" post.pk %}"method="POST">
                                {% csrf_token %}
                                {% bootstrap_form comment_form %}
                                <input type="submit"value="댓글 쓰기"class="btn btn-primary btn-block">
                            </form>
    												<script>
                                $(function(){
                                    var form_id = "post-detail-{{ post.pk }}-comment-form";
                                    $("#" + form_id).submit(function(e){
    e.preventDefault();
    var options = {
                                            success: function(responseText,statusText,xhr,$form){
                                                console.group("ajaxSubmit response");
                                                $("#post-detail-{{ post.pk }}-comment-list").prepend(responseText);
                                                console.log(responseText);
                                                console.log(statusText);
                                                console.log(xhr);
                                                console.log($form);
                                                console.groupEnd();
                                            },
                                            clearForm: true,
                                        }
                                        $(this).ajaxSubmit(options);
                            </script>
    										</div>
                    </div>
                </div>
            </div>
        </div>
    {% endblock %}
    ```
    
    - post_detail에서는 우리가 view 단에서 post와 comment_form을 받아왔다.
    - 해당 포스트의 정보들과 포스트에 달려있는 comment들을 실어주었다.
    - 태그는 Post 모델에 있는 extract_tag_list 함수로 가져온 tag_set을 for문을 이용해 전부 가져와서 하나씩 나열해준다.
    - humanize의 naturaltime을 이용하면 언제 이 글이 만들어졌는지 보다 깔끔하게 쓸 수 있다.
        - *`[https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/](https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/)`*
    - 그 외의 기능인 좋아요, ajax 댓글 기능은 더 세부적으로 다루기 위해 여기서는 다루지 않겠다.
- **url**
    
    ```python
    path('post/<int:pk>/', views.post_detail, *name*='post_detail')
    ```
    

## 좋아요 기능

- **view**
    
    ```python
    @login_required
    def post_like(request,pk):
        post = get_object_or_404(Post,pk=pk)
        post.like_user_set.add(request.user)
    		messages.success(request, f"{post}를 좋아합니다.")
        redirect_url =request.META.get("HTTP_REFERER", "root")
    		return redirect(redirect_url)
    
    @login_required
    def post_unlike(request,pk):
        post = get_object_or_404(Post,pk=pk)
        post.like_user_set.remove(request.user)
        messages.success(request, f"{post}의 좋아요를 취소합니다.")
        redirect_url =request.META.get("HTTP_REFERER", "root")
    		return redirect(redirect_url)
    ```
    
    - url을 통해서 받아온 pk로 어떤 포트스인지 가져온다.
    - ManyToMany 필드인 like_user_set 필드에 좋아요를 누른 유저를 집어넣어준다.
    - HTTP_REFERER이 있다면 해당 주소를 redirect_url로 주고, 없다면 root 페이지로 이동하게 설정해준 후 redirect 시켜준다.
- template
    
    ```html
    <div>
        {% if post|is_like_user:user %}
            <a href="{% url "instagram:post_unlike" post.pk %}"style="color: inherit;">
                <i class="fa-solid fa-heart"></i>
    </a>
        {% else %}
            <a href="{% url "instagram:post_like" post.pk %}"style="color: inherit;">
                <i class="fa-regular fa-heart"></i>
            </a>
        {% endif %}
    </div>
    ```
    
    - html에서는 파라미터를 따로 줄 수 없다.
    - 하지만 이것을 가능하게 하기 위한 방법이 있다.
        - [https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/](https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/)
        - templatetags 라는 폴더를 만들고 두가지 파일을 만들어준다.
            
            ![Untitled](%E1%84%80%E1%85%B5%E1%84%82%E1%85%B3%E1%86%BC%20%E1%84%89%E1%85%A5%E1%86%AF%E1%84%86%E1%85%A7%E1%86%BC(%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB%20%E1%84%8F%E1%85%A9%E1%84%83%E1%85%B3)%200b92115fca0542a3a6066b439d2ff1ad/Untitled.png)
            
        - 그 후, 사용 템플릿에서 {% load instagram_tags %} 로 불러와준다.
            
            ```python
            # instagram/templatetags/instagram_tags.py
            from django import template
            register = template.Library()
            
            @register.filter
            def is_like_user(post, user):
                return post.is_like_user(user)
            ```
            
            - 해당 양식대로 쓴다.
            - 우리가 필요한 파라미터는 post와 user이다.
            
            ```html
            {% if post|is_like_user:user %}
            혹은
            {{ post|is_like_user:user }}
            ```
            
            - 장고 태그를 이용해서 쓸 때와 그냥 쓸 때이다.
            - 첫번째 인자를 앞에 써주고 | 이 기호를 넣어준 후, instagram_tags.py에서 선언한 함수를 써준다.
            - 그리고 두번째 인자를 : 을 붙인 후 써준다.
            
            ```python
            def is_like_user(self,user):
            		return self.like_user_set.filter(pk=user.pk).exists()
            ```
            
            - is_like_user 함수는 해당 포스트의 like_user_set에서 해당 유저가 좋아요를 누른적이 있는지 없는지를 판별해주는 함수이다.
    - 그리고 Font Awesome 홈페이지에서 받아온 아이콘을 사용한다.
        - 사용 방법
            - font awesome 홈페이지 접속 후, 로그인
            - kits 클릭 후, kit을 하나 만들어준다.
            - How to Use에 들어가면 Add Your Kit’s Code to a Project라고 나온다.
                
                ![Untitled](%E1%84%80%E1%85%B5%E1%84%82%E1%85%B3%E1%86%BC%20%E1%84%89%E1%85%A5%E1%86%AF%E1%84%86%E1%85%A7%E1%86%BC(%E1%84%80%E1%85%AE%E1%84%92%E1%85%A7%E1%86%AB%20%E1%84%8F%E1%85%A9%E1%84%83%E1%85%B3)%200b92115fca0542a3a6066b439d2ff1ad/Untitled%201.png)
                
            - 해당 코드를 복사 후, 최상위 layout 파일로 간다.
            - 위쪽에 https만 뺀 나머지 코드를 붙여넣기 해준다.
            - 그리고 다시 홈페이지로 돌아온다.
            - Icons 클릭 후 원하는 아이콘 검색
            - 검색해서 나온 아이콘 클릭 후, html 코드를 복사해서 쓰고 싶은 템플릿에 붙여넣기 해준다.
    - 우리는 좋아요 아이콘을 클릭할 수 있게 해줘야 하기 때문에 a 태그를 사용하였다.
    - 하지만 a 태그를 사용하면 링크처럼 파란색으로 색깔이 칠해지기 때문에 style=”color: inherit;” 을 주어서 색깔이 바뀌지 않게 해준다.
    - 좋아요를 누른 유저라면 하트가 칠해져있기 때문에 해당 아이콘을 클릭하면 post_unlike 태그를 가진 url로 이동하게 해준다.
    - 누르지 않은 유저라면 하트가 칠해져있지 않기 때문에 클릭하면 post_like 태그를 가진 url로 이동하게 해준다.
    - 그래서 해당 포스트에서 해당 유저가 좋아요를 눌렀는지 안눌렀는지 여부에 따라 빈하트로 보일지 채워진 하트로 보일지 구현한 코드이다.
- **url**
    
    ```python
    path('post/<int:pk>/like/', views.post_like,name='post_like'),
    path('post/<int:pk>/unlike/', views.post_unlike,name='post_unlike')
    ```
    

## 코멘트 모델

- **field**
    
    ```python
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    message = models.TextField()
    
    ```
    
- **BaseModel**
    
    ```python
    class BaseModel(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        class Meta:
            abstract = True
    
    class Comment(BaseModel):
    	...
    	...
    ```
    
    - created_at과 updated_at은 모든 모델에서 적용하는 필드이다.
    - 계속 쓰기 귀찮으니 따로 BaseModel이라는 class를 선언해서 필요한 모델에 상속해주면 된다.
    - 그리고 abstract = True로 만들어주면 db 테이블이 따로 만들어지지 않는다.
        - 하지만 불러올 수는 있다!

## 댓글 기능

- **view**
    
    ```python
    @login_required
    def comment_new(request, post_pk):
        post = get_object_or_404(Post,pk=post_pk)
        if request.method == "POST":
            form = CommentForm(request.POST,request.FILES)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author =request.user
                comment.save()
    						if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
    								return render(request, "instagram/_comment.html", {
                        "comment": comment,
                    })
                return redirect(comment.post)
        else:
            form = CommentForm()
        return render(request, "instagram/comment_form.html", {
            "form": form
        })
    
    ```
    
    - url을 통해서 post_pk 값을 받아준다.
        - 그냥 pk로 쓰면 commet_pk와 겹칠 수도 있기 때문에 post_pk라고 써줌.
    - POST
        - form을 지정해준다.
        - form의 유효성 검사
            - 이것또한 포스팅 기능과 같게 commit을 False로 주어서 post 필드와 author 필드를 사용자가 정하는 것이 아니게 따로 저장해준다.
            - save
            - request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                - is_ajax 기능은 장고가 4버전을 넘어오면서 사라졌다.
                - 그래서 is_ajax 기능을 장고 4버전에서 쓰고 싶다면
                    - ajax로 댓글을 쓰면 전체 페이지를 응답으로 주지 말고 코멘트 하나를 따로 html 파일로 만들어서 응답하게 해줘야 새로고침이 안되고 작성한 댓글이 업데이트가 된다.
            - 만약 ajax 통신이 아니라면 post 모델에서 get_absolute_url을 구현해놨기 때문에 comment.post로 redirect 해준다.
    - GET
        - CommentForm을 불러온다.
- **form**
    
    ```python
    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ['message']
            widgets = {
                "message": forms.Textarea(attrs={"rows": 2}),
            }
    ```
    
    - view 단에서 commit = False로 작성자와 게시글을 따로 저장해준다.
    - 그러므로 필요한 필드는 message 하나이다.
    - widgets으로 텍스트 상자를 넓혀준다.
- **template**
    - comment_form.html
    
    ```html
    {% extends "instagram/layout.html" %} 
    {% load bootstrap4 %} 
    {% block content %}
    <div class="container">
      <div class="row">
        <div class="col-sm-6 offset-sm-3">
          {% include "_form.html" with form_title="댓글 쓰기" submit_label="댓글 쓰기" %}
        </div>
      </div>
    </div>
    {% endblock %}
    
    ```
    
    - _comment.html
    
    ```html
    {% load humanize %}
    <div class="comment">
      <strong>{{ comment.author }}</strong>
      {{ comment.message }}
      <small class="text-muted">{{ comment.created_at|naturaltime }}</small>
    </div>
    
    ```
    
    - humanize는 현재 인스타에서 created_at이나 updated_at을 몇일 몇시간 몇분 이런식으로 나타내는 것이 아닌 3 days ago, 10초전 이런식으로 나타내는 것.
    - _comment.html은 ajax 통신으로 댓글 기능을 구현할 때 현재 작성한 댓글만 업데이트 시키기 위해서 쓰는 파일이다.
- **url**
    
    ```python
    path('post/<int:post_pk>/comment/new',
         views.comment_new,name='comment_new')
    ```
    

## 댓글 기능(ajax)

- **view**
    
    ```python
    @login_required
    def comment_new(request,post_pk):
        post = get_object_or_404(Post,pk=post_pk)
        if request.method == "POST":
            form = CommentForm(request.POST,request.FILES)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author =request.user
                comment.save()
    						if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
    								return render(request, "instagram/_comment.html", {
                        "comment": comment,
                    })
                return redirect(comment.post)
        else:
            form = CommentForm()
        return render(request, "instagram/comment_form.html", {
            "form": form
        })
    ```
    
    - [위에 댓글 기능](https://www.notion.so/8dc0d44b118a42d5b762bab56ff60b4c)에서 설명했던 view이다.
    - [ajax란?](https://99geo.tistory.com/65) 참고하도록 하자
- **template**
    
    ```jsx
    <div class="card-footer">
            <form id="post-{{ post.pk }}-comment-form"action="{% url "instagram:comment_new" post.pk %}"method="POST">
                {% csrf_token %}
                {% bootstrap_form comment_form %}
                <input type="submit"value="댓글 쓰기"class="btn btn-primary btn-block">
            </form>
    				<script>
                $(function(){
                    var form_id = "post-{{ post.pk }}-comment-form";
                    $("#" + form_id).submit(function(e){
    e.preventDefault();
    										var options = {
                            success: function(responseText,statusText,xhr,$form){
                                console.group("ajaxSubmit response");
                                $("#post-{{ post.pk }}-comment-list").prepend(responseText);
                                console.log(responseText);
                                console.log(statusText);
                                console.log(xhr);
                                console.log($form);
                                console.groupEnd();
                            },
                            clearForm: true,
                        }
                        $(this).ajaxSubmit(options);
    })
                })
            </script>
    </div>
    ```
    
    - 일단 댓글 기능만 긁어온 html 코드이다.
    - ajax를 사용하기 위해서는 jquery.form을 다운받아와야 한다.
        - [jquery.form링크](https://malsup.github.io/jquery.form.js)
            - Ctrl + s 를 눌러서 파일을 다운받고 static 파일에 넣어준다.
            - 그리고 최상위 layout 파일로 가서 추가해준다.
                
                ```html
                <script *src*="{% static "jquery.form.js" %}"></script>
                ```
                
                - 그 후, 페이지에 가서 F12를 눌러서 네트워크를 열고 jquery를 치면 import가 된 걸 확인할 수 있다.
                - [ajax 사용 홈페이지](https://malsup.com/jquery/form/#ajaxForm)에 가서 문서를 참고하도록 하자.
                - $(document).ready(function() 과 위의 $(function()은 같은 문법이다. 축약 문법임.
    - ajax를 하려고 하는 곳은 댓글 폼이다.
    - 그렇기 때문에 댓글을 불러오는 html 코드에서 form의 id를 지정해주고, options의 success 쪽에 $(”#post-{{ [post.pk](http://post.pk) }}-comment-list”).prepend(responseText); 이 코드를 넣어준다. 물론 안에 들어가는 post-{{ post.pk }}-comment-list 이 부분이 코멘트를 불러오는 form 의 id이다.
    - $(this).ajaxSubmit(options); 를 한다면 jquery를 통해서 submit이 되는 것이다.
    - 거짓으로 리턴한다던지, 이벤트 객체 e로 e.preventDefault로 호출을 해주면 이벤트가 더이상 전파되지 않고 현재 상황에서 멈추게 된다.

## 유저 페이지 기능

- **view**
    
    ```python
    def user_page(request, username):
        page_user = get_object_or_404(
            get_user_model(), username=username, is_active=True)
    		post_list = Post.objects.filter(author=page_user)
        post_list_count = post_list.count()
    
    		if request.user.is_authenticated:
            is_follow = request.user.following_set.filter(pk=page_user.pk).exists()
    		else:
            is_follow = False
    
        return render(request, "instagram/user_page.html", {
            "page_user": page_user,
            "post_list": post_list,
            "post_list_count": post_list_count,
            "is_follow": is_follow,
        })
    ```
    
    - model은 get_user_model()로 불러온 User 모델을 사용하고 url에서 username을 이용해 해당 username과 같은 그리고 활성화 되어 있는 user 모델을 불러온다.
    - 유저 페이지이기 때문에 불러온 user인 page_user가 작성한 post_list를 불러온다.
    - 그리고 해당 게시글의 갯수를 세기 위해 count 함수를 이용해 post_list_count도 세팅해준다.
    - 만약 user가 로그인이 되어 있는 인증 받은 유저라면 팔로우를 하기 위한 is_follow 변수를 True로 만들어준다.
        - exists() 함수는 만약 존재한다면 True를 아니라면 False를 반환해준다.
    - page_user와 post_list, post_list_count, is_follow를 템플릿으로 넘겨준다.
- **template**
    
    ```html
    {% extends "instagram/layout.html" %}
    {% load thumbnail %}
    {% block content %}
        <div class="container">
            <div class="row pt-5 pb-5">
                <div class="col-sm-3"style="text-align: center;">
                    <img src="{{ page_user.avatar_url }}"class="rounded-circle"style="width: 160px;" />
                </div>
                <div class="col-sm-9">
                    {{ page_user.username }}
                    {% if user == page_user %}
                        <a href="{% url "accounts:profile_edit" %}"class="btn btn-secondary btn-sm">
                            Edit Profile
                        </a>
                    {% else %}
                        {% if is_follow %}
                            <a href="{% url "accounts:user_unfollow" page_user.username %}">
                                Unfollow
                            </a>
                        {% else %}
                            <a href="{% url "accounts:user_follow" page_user.username %}">
                                Follow
                            </a>
                        {% endif %}
                    {% endif %}
                    <hr/>
                    {{ post_list_count }} posts, {{ page_user.follower_count }} followers, {{ page_user.following_count }} following
                    <hr/>
                    {{ page_user.name }}
                </div>
                <hr/>
                <div class="col-sm-12">
                    <div class="container">
                        <div class="row">
                            {% for post in post_list %}
                            <div class="col-sm-4 mb-3">
                                <a href="{% url "instagram:post_detail" post.id %}">
                                    <img src="{% thumbnail post.photo 512x512 crop %}"alt="{{ post.caption }}"style="width: 100%;"/>
                                </a>
                            </div>
    {% endfor %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    {% endblock %}
    ```
    
    - 일단 유저 페이지에 들어간 사용자가 해당 유저인지 아닌지를 판별을 해야한다.
        - 왜냐면 해당 유저라면 follow 버튼이 있는 것이 아닌 자신의 프로필을 수정하는 버튼 Edit Profile 이 나오게 해줘야 하기 때문.
    - 만약 해당 유저가 아니라면?
        - 팔로우를 한 유저인지 아닌지 판별을 해야한다.
        - 그걸 위해서 우리가 view 단에서 is_follow 변수를 사용한 것이다.
            - is_follow가 True이면?
                - 팔로우를 한 유저이기 때문에 Unfollow로 보여주고 눌렀을 때 url을 unfollow를 수행해주는 url로 설정.
            - False이면?
                - 팔로우를 하지 않은 유저이기 때문에 Follow로 보여주고 눌렀을 때 url을 follow를 수행해주는 url로 설정.
    - east-thumbnail 사용법
        - pip install easy-thumbnails 를 하고 INSTALLED_APPS에 추가
        - [manage.py](http://manage.py) migrate easy_thumbnails 실행
        - 사용하고자 하는 template에 {% load thumbnail %} 불러오기
            
            ```html
            <img src="{% thumbnail post.photo 512x512 crop %}"alt="{{ post.caption }}"style="width: 100%;"/>
            ```
            
        - 태그 뒤에 thumbnail을 주고 불러오고자 하는 이미지 주소 그리고 몇 곱하기 몇의 크기로 썸네일을 정사각형으로 만들지 쓰고 뒤에 crop을 붙여주면 된다.
- **url**
    
    ```python
    re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page, *name*='user_page')
    ```
    
    - username을 url로 쓰는 방법이다.

## 부가 기능

- **날짜 필터링 기능**
    
    *`https://docs.djangoproject.com/en/4.1/ref/contrib/humanize/`*
    
    [사용법 예시](https://www.notion.so/0b92115fca0542a3a6066b439d2ff1ad)
    
- **html에서 파라미터 사용하기**
    
    *`https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/`*
    
    [사용법](https://www.notion.so/8dc0d44b118a42d5b762bab56ff60b4c)
    
- **아이콘 사이트**
    
    [https://fontawesome.com/](https://fontawesome.com/)
    
    [사용법](https://www.notion.so/8dc0d44b118a42d5b762bab56ff60b4c)
    
- **썸네일 정사각형을 위한 crop**
    
    [https://github.com/SmileyChris/easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails)
    
    [사용법](https://www.notion.so/8dc0d44b118a42d5b762bab56ff60b4c)

