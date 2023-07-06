from .controller import PostController
from .repository import PostRepository
from post.models import Post, Comment, Like
from rest_framework import serializers


class AddPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField(max_length=250, allow_blank=False)
    date = serializers.DateField(read_only=True)
    image = serializers.ImageField(required=False)

    def validate(self, attrs):
        user_id = self.context.get('user_id')
        response = PostController.add_post(attrs, user_id)
        return response
