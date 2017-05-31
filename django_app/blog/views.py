from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def main_view(request):
    post = Post.objects.all()
    print(post[0])
    context = {
        'posts': post
    }
    return render(request, 'base/base.html', context)

def post_add_view(request):
    return HttpResponse('post_add_view가 연결되었습니다.')