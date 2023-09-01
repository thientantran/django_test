from .views import PostList, PostDetail, PostListDetailfilter,CreatePost,AdminPostDetail,EditPost,DeletePost
#from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.routers import DefaultRouter
app_name = 'blog_api'


# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls
# LINK MUỐN THÊM ROUTER: https://stackoverflow.com/questions/56149121/django-the-actions-argument-must-be-provided-when-calling-as-view-w
# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate')
# ]
urlpatterns = [
    path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    # path('posts/', PostDetail.as_view(), name='detailcreate'),
    # http://localhost:8000/api/posts/?slug=test
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    # http://localhost:8000/api/search/?search=te
    path('', PostList.as_view(), name='listcreate'),

# Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]