from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
# add permission rules
from rest_framework.permissions import SAFE_METHODS,IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

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


# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer
#     def get_object(self, queryset=None, **kwargs):
#         # sử dụng cái này để lấy 1 object có tên như theo query,
#         # chú ý là sẽ phải giống như khi query, phân biệt cả chữ thường và chữ hoa
#         item = self.kwargs.get('pk')
#         print(item)
#         return get_object_or_404(Post, id=item)
#     # Define Custom Queryset, khi mà chỉ có api mà ko có key để query thì vào đây, còn khi có query key thì nhảy vào cái get_object
#     def get_queryset(self):
#         # filter posts theo author
#         try:
#             user = self.request.user
#             return Post.objects.filter(author=user)
#         except:
#             return []

# api "/api/" nó có nhiều nhánh ở trong nữa, thì nên tạo mỗi nhánh
class PostList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        try:
            user = self.request.user
            return Post.objects.filter(author=user)
        except:
            return []

class PostDetail(generics.ListAPIView):
    # chỗ này sử dụng listAPi view thì ra, nhưng trả về dạng list, còn dùng cái Retrieve thì nó lại ko ra
    # do đó ko thể get 1 oject để sửa hoặc xoá được, (do đang dùng listAPI)
    # thì do dùng objects.filter nên mặc định trả về list, và ko hỗ trợ trả về 1 object để xoá, sửa, do đó ko dùng cho retrieve được
    serializer_class = PostSerializer

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        # chỗ này có thể dụng nhiều variables
        print(slug)
        return Post.objects.filter(slug=slug)

# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#     # sử dụng viewset sẽ ko có các get, póst, mà sẽ dùng nhưng method list, retrieve được built sẵn để thực hiện
#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    # class PostList(viewsets.ModelViewSet):
    #     permission_classes = [IsAuthenticated]
    #     queryset = Post.postobjects.all()
    #     serializer_class = PostSerializer

    # class PostDetail(viewsets.ModelViewSet, PostUserWritePermission):
    #     permission_classes = [PostUserWritePermission]
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer
# class PostList(generics.ListCreateAPIView):
#     # permission_classes = [IsAdminUser]
#     # permission_classes = [IsAuthenticatedOrReadOnly]
#     permission_classes = [IsAuthenticated]
#     # permission_classes = [DjangoModelPermissions]
#     # cái này là khi mình tạo user, có đưa vào 1 cái group và có add các permissions vào rồi, giờ nó tuân theo cái này
#     # nhận được phương thức list hoặc create
#     queryset = Post.postobjects.all()
#     # collect data from database
#     serializer_class = PostSerializer
#     # serializer sẽ convert data of cái queryset và model thành data format của python,
#     # để chuyển về dạng json, dễ dàng khi response về frontend
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     # nhận được phương thức Retrieve hoặc destroy
#     queryset = Post.objects.all()
#     # cái phương thức này mặc định nó sẽ retrive và lấy theo Id
#     serializer_class = PostSerializer

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