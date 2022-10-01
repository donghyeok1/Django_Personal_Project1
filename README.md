# Django_Personal_Project1

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
                  {% if form_title %}
                  <div class="card-header">{{ form_title }}</div>
                  {% endif %}
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