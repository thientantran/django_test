from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    # nhận được phương thức list hoặc create
    queryset = Post.postobjects.all()
    # collect data from database
    serializer_class = PostSerializer
    # serializer sẽ convert data of cái queryset và model thành data format của python,
    # để chuyển về dạng json, dễ dàng khi response về frontend


class PostDetail(generics.RetrieveDestroyAPIView):
    # nhận được phương thức Retrieve hoặc destroy
    queryset = Post.objects.all()
    # cái phương thức này mặc định nó sẽ retrive và lấy theo Id
    serializer_class = PostSerializer

""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""