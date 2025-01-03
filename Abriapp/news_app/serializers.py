from rest_framework import serializers
from .models import User, News, Comment, Like


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'mobile_number', 'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
class NewsSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()

    class Meta:
        model = News
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = '__all__'
