from django.urls import path
from .views import UserRegistrationView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AddCommentView, AddLikeView
from .views import NewsListView, NewsDetailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('news/<int:news_id>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('news/<int:news_id>/like/', AddLikeView.as_view(), name='add_like'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
