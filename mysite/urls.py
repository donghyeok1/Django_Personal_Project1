from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic import TemplateView
from django_pydenticon.views import image as pydenticon_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('instagram.urls')),
    path('identicon/image/<path:data>/', pydenticon_image, name='pydenticon_image'),
    # pydenticon을 쓰기위한 순서
    # pip install django-pydenticon
    # common.txt에 pillow와 django-pydenticon 추가
    # pillow는 이미지 관련이다.
    # settings에 app에 추가
    # 최상단 url 바꾸기
    # 위의 코드처럼 바꾸기
    # 그리고 다시 common 세팅에 가서 가장 상단에
    # import collections
    # if not hasattr(collections, 'Callable'):
    #     collections.Callable = collections.abc.Callable
    # 추가 해주기!
    # 각 유저마다 다른 디폴트 유저 이미지를 가져오게 해줌.
    # 이렇게 해서 해당 url에 특정 문자를 입력하면 문자에 해당하는 각기 다른 이미지를 준다.
    # 우리는 사용자 닉네임에 해당하는 문자를 입력할 것이다. 예를 들면 img src에 "pydenticon_image" user.username 이런 식으로
    # 그리고 나서 layout.html에 가서 적용을 해보자!
    path('', login_required(TemplateView.as_view(template_name='root.html')), name='root'),
]
# 깃 브랜치 트리 테스트
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
	    path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


