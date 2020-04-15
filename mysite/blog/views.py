from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_objects_or_404(Post, slug=post,
                                    status='puglished',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)

    return render(request, 'blog/post/detail.html', {'post': post})
