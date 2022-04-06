from rest_framework.response import Response
from rest_framework.decorators import api_view
from reddit.models import Article
from .sterillizers import ArticleSerializer

@api_view(['GET'])
def getData(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addArticle(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)