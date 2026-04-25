from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='Название поста',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Придумайте короткое название...',
            'maxlength': '100',
            'class': 'title-input'
        })
    )

    text = forms.CharField(
        label='Текст поста',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Напишите текст публикации...',
            'class': 'text-input'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
        labels = {
            'image': 'Изображение',
        }


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Напишите комментарий...'
        })
    )

    class Meta:
        model = Comment
        fields = ['text']


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'placeholder': 'Введите логин'})
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
