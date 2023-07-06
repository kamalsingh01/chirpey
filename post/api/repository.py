from post.models import Post, Comment, Like
from user_app.models import UserModel
from datetime import datetime


class PostRepository:

    @staticmethod
    def add_post(attrs, user_id):
        user = UserModel.objects.get(id=user_id)
        if 'image' in attrs:
            image = attrs['image']
        else:
            image = None
        post = Post(
            content=attrs['content'],
            date=datetime.now(),
            image=image,
            user=user,
        )
        post.save()
        return {}

    @staticmethod
    def get_post(post_id):
        post = Post.objects.get(id=post_id)
        return post

    @staticmethod
    def update_post(attrs, post_id):
        post = Post.objects.get(id=post_id)
        image = attrs['image']
        post.content = attrs.get('content', post.content)
        post.image = image
        post.date = datetime.now()
        post.save()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.objects.get(id=post_id)
        post.delete()
        return True

    @staticmethod
    def get_all_posts():
        posts = Post.objects.all()
        return posts
