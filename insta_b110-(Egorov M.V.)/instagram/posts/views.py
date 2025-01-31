from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from .models import Post


def index(request):
    # запрос к базе данных
    posts = Post.objects.all().annotate(
        likes_count=Count('likes')
    ).order_by(
        '-likes_count'
    )[:10]
    # формирует ответ
    output = render_to_string('posts/index.html', {'posts': posts})
    return HttpResponse(output)


def lenta_of_posts(request):
    user = request.user
    if user.is_authenticated:
        # для авторизованных пользователей показываем записи друзей
        friends = user.friends.all()
        posts = Post.objects.filter(author__target_friends__in=friends).annotate(
            likes_count=Count('likes')
        )
        return render(request, 'posts/lenta_of_posts.html', {'posts': posts})
    else:
        # для неавторизованных ошибка
        raise PermissionDenied("У неавторизованных пользователей нет друзей")


def post_detail(request, post_pk):
    # try:
    #     post = Post.objects.annotate(
    #             likes_count=Count('likes')
    #         ).get(pk=post_pk)
    #     response = f"<div>pk: {post.pk}| name: {post.name}| likes: {post.likes_count}</div>"
    # except Post.DoesNotExist:
    #     raise Http404("Такого поста нет")

    post = get_object_or_404(Post, pk=post_pk)
    response = f"<div>pk: {post.pk}| name: {post.name}| likes: {post.count_of_likes}</div>"
    return HttpResponse(response)