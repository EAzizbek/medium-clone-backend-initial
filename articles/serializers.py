from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article, Topic
from .models import Clap

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

class ClapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clap  # Replace with the correct model if not Clap
        fields = '__all__'  # Or specify fields explicitly, e.g., ['user', 'article', 'count']

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'summary', 'content', 'author', 'topics', 'created_at', 'updated_at']  # Adjust fields as needed
        depth = 1  # Optional: to include nested details for relationships, like author and topics
