from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Article

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(MAX_LENGTH=100)
#     image = serializers.ImageField()
#     date = serializers.DataTimeFiled()
    
#     def create(self, validated_data): 
#         return Article.objects.create(validated_data)
    
#     def update(self, instance, validated_data)
#         instance.title = validated_data.get('title', instance.title)
#         instance.image = validated_data.get('image', instance.image)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Article
        fields = '__all__'
