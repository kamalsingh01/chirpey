from .controller import PostController
from .repository import PostRepository
from post.models import Post, Comment, Like
from rest_framework import serializers
from datetime import datetime


class AddPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField(max_length=250, allow_blank=False)
    date = serializers.DateTimeField(default=datetime.now)
    image = serializers.ImageField(default=None, required=False)

    def validate(self, attrs):
        user_id = self.context.get('user_id')

        response = PostController.update_post(attrs, user_id)
        return response


class PostUpdateSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=250,required=False)
    edited_at = serializers.DateTimeField(default=datetime.now)
    image = serializers.ImageField(allow_null=True,required=False)  #null for removing photo, pass it as null.

    def validate(self, attrs):
        user_id = self.context.get('user_id')
        post_id = self.context.get('post_id')
        response = PostController.update_post(attrs, user_id, post_id)
        return response


class PostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'content', 'date', 'image', 'user']
