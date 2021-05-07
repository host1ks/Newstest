from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Post, Comment, Upvote
from .serializers import PostSerializer, UpvoteSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UpvoteView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
