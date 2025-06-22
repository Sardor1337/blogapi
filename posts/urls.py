from django.urls import path
from .views import PostListCreateView, PostDetailView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_list_create'),  # GET /posts, POST /posts
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),   # GET, PUT, DELETE /posts/{id}
]
