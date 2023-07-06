from django.shortcuts import render
from rest_framework import response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import AddPostSerializer, PostResponseSerializer, PostUpdateSerializer
from user_app.api.controller import UserController
from post.models import Post
from .controller import PostController


class AddPostView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddPostSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        serializer = self.get_serializer(data=request.data, context={'user_id': user_id})
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {
                "msg": "Post added successfully",
                **serializer.validated_data,
            }
        )


class PostView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostResponseSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostResponseSerializer
        if self.request.method == 'PATCH':
            return PostUpdateSerializer
        return None

    def get(self, request, post_id, *args, **kwargs):
        user_id = request.user.id
        try:
            post = Post.objects.get(id=post_id, user_id=user_id)
            serializer = self.get_serializer(post)
            return response.Response(serializer.data)
        except Post.DoesNotExist:
            return response.Response({
                "msg": "Post doesn't exist for the user"
            })

    def patch(self, request, post_id, *args, **kwargs):
        user_id = request.user.id
        serializer = self.get_serializer(data=request.data, context={'user_id' : user_id, 'post_id' : post_id})
        serializer.is_valid(raise_exception=True)
        return response.Response({
            "msg" : "Post updated successfully"
        }, status=status.HTTP_200_OK
        )


    def delete(self, request, post_id, *args, **kwargs):
        user_id = request.user.id
        if PostController.delete_post(post_id, user_id):
            return response.Response(
                {
                    "msg": "Post Deleted"
                },
                status=status.HTTP_202_ACCEPTED
            )


class GetPostsView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        serializer = PostResponseSerializer(PostController.get_all_posts(user_id), many=True)
        return response.Response(serializer.data)
