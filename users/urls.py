from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, MeView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', MeView.as_view(), name='auth_me'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user_detail'),
]