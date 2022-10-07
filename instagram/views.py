from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from instagram.forms import PostForm, CommentForm
from .models import Tag, Post


@login_required
def index(request):
    # timesince = timezone.now() - timedelta(days=3)
    # 최근 시간에서 3일의 시간을 뺀!

    # post_list = Post.objects.filter(author__in=request.user.following_set.all())
    # author__in 은 author가 오른쪽 값들에 포함이 되어있느냐 라는 뜻
    # author = ~~.all()을 하면 1대 다수여서 안됨
    # 근데 이러면 자기 자신은 following_set에 안들어있기 때문에 빠지게 됨.
    # 이럴때는 or를 써야하는데 Q객체를 이용함!
    post_list = Post.objects\
        .filter(
            Q(author=request.user)
            |
            Q(author__in=request.user.following_set.all())
        )
    # .filter(
    #     created_at__gte=timesince # greater than equal
    # )
    # 최근 시간에서 3일을 뺀 시간보다 큰 포스팅만 가져오겠다!
    suggested_user_list = get_user_model().objects.all().exclude(
        pk=request.user.pk).exclude(pk__in=request.user.following_set.all())[:3]
    # exclude는 제외하겠다는 뜻 필터와 비슷함.
    # 만약 팔로우를 하면 사이드 바에 이름이 없어지게 하는 것임.
    # 다 보여주는 것이 아닌 3명까지만 보여주는것!
    comment_form = CommentForm()
    return render(request, "instagram/index.html", {
        "suggested_user_list": suggested_user_list,
        "post_list": post_list,
        "comment_form": comment_form,
    })


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # commit = True이면 필수 필드인 author 없이 인스턴스를 저장하기 떄문에 오류 발생!
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list())
            # ManytoMany field에서는 add 명령어를 통해 한개씩 넘길 수 있는데 넘기는 인자가 리스트니깐 *로 한번에 좌르륵 넘기기~
            # save를 먼저 해야 이 관계가 성립한다는데 이해 못함
            # TODO 나중에 구글링 해보기!
            messages.success(request, "포스팅을 저장했습니다.")
            return redirect(post)
        # TODO 이해 못함 알바 갔다와서 다시보기
    #     redirect를 하려면 usermodel에서 한것처럼 get_absolute_url이 있어야함.

    else:
        form = PostForm()

    return render(request, "instagram/post_form.html", {
        "form": form,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    # if request.is_ajax(): 이건 장고 4버전부터 없어짐
    return render(request, "instagram/post_detail.html", {
        "post": post,
        "comment_form": comment_form,
    })


@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like_user_set.add(request.user)
    # 좋아요를 처리하기 위해서는 _post_card단에 가서 좋아요라는 링크를 걸어줘야함.
    messages.success(request, f"{post}를 좋아합니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    # HTTP_REFERE이 있으면 가져오고 없으면 root를 가져오겠다.
    return redirect(redirect_url)

@login_required
def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like_user_set.remove(request.user)
    messages.success(request, f"{post}의 좋아요를 취소합니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    # HTTP_REFERE이 있으면 가져오고 없으면 root를 가져오겠다.
    return redirect(redirect_url)


def user_page(request, username):
    page_user = get_object_or_404(
        get_user_model(), username=username, is_active=True)
    # 현재 접근이 허용된 사람만 보겠다.
    # post_list = page_user.my_post_set.all()
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count()
    # 실제 데이터베이스에 count 쿼리를 던지게 됨.
    # len(post_list)를 쓰게 되면 리스트의 갯수가 많을 떄 느리게 동작함!

    if request.user.is_authenticated:
        is_follow = request.user.following_set.filter(pk=page_user.pk).exists()
        # 로그인이 되어있으면 User 객체, 안되어잇으면 AnonymousUser 객체
    else:
        is_follow = False

    return render(request, "instagram/user_page.html", {
        "page_user": page_user,
        "post_list": post_list,
        "post_list_count": post_list_count,
        "is_follow": is_follow,
    })


@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            # if request.is_ajax(): 이건 장고 4버전부터 없어짐
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                # 이게 is_ajax 기능을 4버전에서 이렇게 씀
                # ajax로 댓글을 썻으면 전체 페이지를 응답으로 주지말고 코멘트 하나를 따로
                # html로 만들어서 응답하게 해줘야 새로고침 안되고 댓글이 업데이트가 된다!
                return render(request, "instagram/_comment.html", {
                    "comment": comment,
                })
            return redirect(comment.post)
    else:
        form = CommentForm()
    return render(request, "instagram/comment_form.html", {
        "form": form
    })
