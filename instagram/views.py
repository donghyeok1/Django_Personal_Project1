from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from instagram.forms import PostForm
from .models import Tag, Post


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
    #     redirect를 하려면 usermodel에서 한것처럼 get_absolute_url이 있어야함.

    else:
        form = PostForm()

    return render(request, "instagram/post_form.html", {
        "form" : form,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "instagram/post_detail.html", {
        "post" : post,
    })

def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    # 현재 접근이 허용된 사람만 보겠다.
    post_list = Post.objects.filter(author=page_user)
    post_list_count = post_list.count()
    # 실제 데이터베이스에 count 쿼리를 던지게 됨.
    # len(post_list)를 쓰게 되면 리스트의 갯수가 많을 떄 느리게 동작함!
    return render(request, "instagram/user_page.html", {
        "page_user": page_user,
        "post_list": post_list,
        "post_list_count": post_list_count,
    })