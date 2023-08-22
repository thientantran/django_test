from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
# add permission rules
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        # chỗ này đặt là has_object_permission hoặc has_permission
        # do cái này nó áp dụng cho ọbject nên phải có chữ object
        #https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
        if request.method in SAFE_METHODS:
            # Check permissions for read-only request. Methods: 'GET', 'OPTIONS' and 'HEAD'
            return True
        else:
            # Check permissions for write request
            return obj.author == request.user
        # mấy thằng là tác giả mới có thể xoá hoặc sửa, còn mấy thằng khác chỉ có thể get thôi
class PostList(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # cái này là khi mình tạo user, có đưa vào 1 cái group và có add các permissions vào rồi, giờ nó tuân theo cái này
    # nhận được phương thức list hoặc create
    queryset = Post.postobjects.all()
    # collect data from database
    serializer_class = PostSerializer
    # serializer sẽ convert data of cái queryset và model thành data format của python,
    # để chuyển về dạng json, dễ dàng khi response về frontend


class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
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