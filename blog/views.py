from inspect import trace
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

class ListPost(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data.get("post")
        
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()

        return Response({"success": f"Post '{post}' created successfully"})

class PostView(APIView):
    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id)[0]
        serializer = PostSerializer(post)

        return Response({"post": serializer.data})

class CommentTree:
    def tree(self, comments, nesting_level):
        if not nesting_level:
            return

        data = []

        for comment in comments:
            comment_data = CommentSerializer(comment).data
            comment_data.update({
                "replies": self.tree(comment.child_set.all(), nesting_level - 1)
            })
            
            data.append(comment_data)

        return data

class ListComment(APIView, CommentTree):
    def get(self, request, post_id):
        default_nesting_level = 3
        nesting_level = int(self.request.GET.get("nesting-level", default_nesting_level))

        comments = Comment.objects.filter(post=post_id, parent=None)
        comments_tree = super().tree(comments, nesting_level)

        return Response({
            "comments": comments_tree,
        })

    def post(self, request, post_id):
        comment = {
            "post": post_id,
            "parent": request.data.get("parent"),
            "author": request.data.get("author"),
            "text": request.data.get("text"),
        }
        
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()

        return Response({"success": f"Comment '{comment}' created successfully"})

class CommentView(APIView, CommentTree):
    def get(self, request, post_id, comment_id):
        default_nesting_level = 3
        nesting_level = int(self.request.GET.get("nesting-level", default_nesting_level))

        comment = Comment.objects.filter(id=comment_id)[0]

        return Response({
            "comment": super().tree([comment], nesting_level),
        })
