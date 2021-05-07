from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import PostViewSet, CommentViewSet, UpvoteView

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'comment', CommentViewSet, basename='comment')

app_name = 'main'
urlpatterns = [
    path('upvote/', UpvoteView.as_view()),
]


urlpatterns += router.urls
