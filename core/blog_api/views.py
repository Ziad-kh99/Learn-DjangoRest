from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


# ListCreateAPIView allow us to list or create items.
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer




# RetrieveDestroyAPIView allow us to Retrieve a specific item or destroy/delete a specific item.
class PostDetail(generics.RetrieveDestroyAPIView): 
    queryset = Post.objects.all()
    serializer_class = PostSerializer
