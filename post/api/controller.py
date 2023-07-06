from post.models import Post, Comment, Like
from user_app.models import UserModel
from .repository import PostRepository
from rest_framework import serializers


class PostController:

    @staticmethod
    def add_post(attrs, user_id):
        response = PostRepository.add_post(attrs, user_id)
        return response

    @staticmethod
    def update_post(attrs, user_id, post_id):
        try:
            post=Post.objects.get(id = post_id, user_id = user_id)
            response = PostRepository.update_post(attrs, post_id)
            return response
        except Post.DoesNotExist:
            raise serializers.ValidationError({"error":"Post doesn't exist for the user"})


    @staticmethod
    def delete_post(post_id, user_id):
        try:
            post=Post.objects.get(id = post_id, user_id = user_id)
            response = PostRepository.delete_post(post_id)
            return response
        except Post.DoesNotExist:
            raise serializers.ValidationError({"error":"Post doesn't exist for the user"})


    @staticmethod
    def get_all_posts():
        response = PostRepository.get_all_posts()
        return response