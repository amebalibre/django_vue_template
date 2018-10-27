"""Serializer class."""
from .models.post import Post
from .models.tag import Tag
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    """Tags."""

    class Meta:
        """Meta class."""

        model = Tag
        fields = ('name', 'color')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """Posts."""

    class Meta:
        """Meta class."""

        model = Post
        fields = ('title', 'content', 'pub_date', 'tags')
