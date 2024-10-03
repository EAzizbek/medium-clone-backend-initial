from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article, Topic

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'avatar']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'is_active']

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    topics = TopicSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'topics']

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'topics']
