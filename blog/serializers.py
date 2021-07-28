from django.db.models import fields
from rest_framework import serializers

from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'author']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'parent', 'author', 'text']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
