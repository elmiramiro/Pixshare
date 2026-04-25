from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponseForbidden
from posts.models import Post, Like
from .forms import PostForm, CommentForm, RegisterForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'frontend/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(request, 'frontend/post_detail.html', {
        'post': post,
        'comment_form': comment_form
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Пост успешно создан')
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'frontend/post_create.html', {'form': form})


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Комментарий добавлен')

    return redirect('post_detail', pk=pk)


@login_required
def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Like.objects.get_or_create(author=request.user, post=post)
    messages.success(request, 'Лайк поставлен')
    return redirect('post_detail', pk=pk)


@login_required
def remove_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(author=request.user, post=post).first()
    if like:
        like.delete()
        messages.success(request, 'Лайк убран')
    return redirect('post_detail', pk=pk)

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("Вы не можете редактировать чужой пост")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост обновлён')
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'frontend/post_edit.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("Вы не можете удалить чужой пост")

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Пост удалён')
        return redirect('post_list')

    return redirect('post_detail', pk=pk)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('post_list')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Вы вышли из аккаунта')
    return redirect('post_list')

