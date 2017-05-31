from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Post
from .forms import PostCreateForm
from django.contrib.auth.models import User

user = User.objects.first()


def main_view(request):
    post = Post.objects.all()
    print(post[0])
    context = {
        'posts': post
    }
    return render(request, 'post_list.html', context)


def post_add_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'post_add.html', context)
    elif request.method == 'POST':
        form = PostCreateForm(request.POST)

        if form.is_valid():
            Post.objects.create(
                author=user,
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
            )

        return redirect('post_main')
