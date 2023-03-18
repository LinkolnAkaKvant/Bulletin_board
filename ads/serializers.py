from rest_framework import serializers
from rest_framework.fields import BooleanField
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(required=False)
    author_first_name = serializers.CharField(max_length=50, required=False)
    author_last_name = serializers.CharField(max_length=50, required=False)
    author_image = serializers.ImageField(required=False)
    ad_id = serializers.IntegerField(required=False)

    class Meta:
        model = Comment
        exclude = ['author', 'ad']


class AdSerializer(serializers.ModelSerializer):
    is_published = BooleanField(required=False)

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(required=False)
    author_first_name = serializers.CharField(max_length=50, required=False)
    author_last_name = serializers.CharField(max_length=50, required=False)
    phone = serializers.CharField(max_length=13, required=False)

    class Meta:
        model = Ad
        exclude = ['author', 'created_at']
