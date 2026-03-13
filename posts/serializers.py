from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'image', 'created_at', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'image', 'created_at', 'comments', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'text', 'image']


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Like
        fields = ['id', 'author', 'post', 'created_at']

        