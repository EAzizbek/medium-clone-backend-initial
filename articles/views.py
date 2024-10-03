from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer, ArticleCreateSerializer

class ArticlesView(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ArticleCreateSerializer
        return ArticleSerializer

    def perform_create(self, serializer):
        # Current user as author
        serializer.save(author=self.request.user)