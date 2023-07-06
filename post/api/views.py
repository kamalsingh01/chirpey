from django.shortcuts import render
from rest_framework import response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import AddPostSerializer


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


# class PostView(GenericAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostResponseSerializer
#
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return PostResponseSerializer
#         if self.request.method == 'PATCH':
#             return PostUpdateSerializer
#         return None
#
#     def get(self, request,pk, *args, **kwargs):
#         user_id = request.user.id
#         serializer = self.get_serializer()