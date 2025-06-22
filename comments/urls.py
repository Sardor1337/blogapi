from django.urls import path
from .views import CommentListCreateView, CommentDeleteView

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('comments/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]
