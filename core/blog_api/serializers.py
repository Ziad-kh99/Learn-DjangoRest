from rest_framework import serializers 
from blog.models import Post 


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # 1. define the model:
        model = Post
        # 2. specifiy which fields/attributes we need to serialize:
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')

