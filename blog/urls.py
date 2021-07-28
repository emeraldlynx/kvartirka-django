from typing import List
from django.urls import path, re_path

from .views import ListPost, PostView, ListComment, CommentView

urlpatterns = [
    re_path(r'^api/posts/$', ListPost.as_view(), name='list_post'),
    re_path(r'^api/post/(?P<post_id>\d)/$', PostView.as_view(), name='post'),
    re_path(r'^api/post/(?P<post_id>\d)/comments/$', ListComment.as_view(), name='list_comment'),
    re_path(r'^api/post/(?P<post_id>\d)/comment/(?P<comment_id>\d)/', CommentView.as_view(), name='comment'),
]
