from rest_framework import serializers
from main.models import Post, Comment, Upvote


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    count_upvote = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    @staticmethod
    def get_comments(obj):
        return CommentSerializer(obj.comment_set, many=True).data

    @staticmethod
    def get_count_upvote(obj):
        return len(UpvoteSerializer(obj.upvote_set, many=True).data)


class UpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upvote
        fields = '__all__'
