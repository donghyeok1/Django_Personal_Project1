from django.contrib import messages
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