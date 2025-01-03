from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegistrationSerializer
from .models import User
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from .permissions import IsAdmin

class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdmin]


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import News, Comment, Like
from .serializers import CommentSerializer, LikeSerializer

class AddCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, news=news)
            news.comments_count += 1
            news.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddLikeView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        like, created = Like.objects.get_or_create(user=request.user, news=news)
        if created:
            news.likes_count += 1
            news.save()
            return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            news.likes_count -= 1
            news.save()
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-publish_date')
    serializer_class = NewsSerializer

class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

