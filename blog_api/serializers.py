from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('category', 'id', 'title', 'slug', 'author',
                  'excerpt', 'content', 'status')
        model = Post
        # define what data in the model we want to work with?