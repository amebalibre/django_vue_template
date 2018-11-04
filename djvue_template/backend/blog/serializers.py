"""Serializer class."""
from .models.post import Post
from .models.tag import Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Tags."""

    class Meta:
        """Meta class."""

        model = Tag
        fields = ('name', 'color')


class PostSerializer(serializers.ModelSerializer):
    """Posts."""

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        """Meta class."""

        model = Post
        fields = ('title', 'content', 'pub_date', 'tags')
