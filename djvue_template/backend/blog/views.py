"""Dummy docstring."""
from rest_framework import viewsets
from . import serializers
from .models.post import Post
from .models.tag import Tag


class TagViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = Post.objects.all().order_by('-pub_date')
    serializer_class = serializers.PostSerializer
