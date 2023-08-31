from .views import PostList, PostDetail, PostListDetailfilter
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
]