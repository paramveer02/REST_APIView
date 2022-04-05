from django.http import Http404
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleView(APIView):
    """
    TODO:Document
    """

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get("article")
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response(
            {"success": "Article '{}' created successfully".format(article_saved.title)}
        )


class ArticleDetailView(APIView):
    """
    TODO:Document
    """

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response(
                {
                    "success": "Article '{}' updated successfully".format(
                        article_saved.title
                    )
                },
            )

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(
            {"message": "Article with id `{}` has been deleted.".format(pk)}, status=204
        )
