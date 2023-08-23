from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    # chỗ này ko hiểu lắm, nó nói là, bình thường vào web, thì thấy tất cả post
    # giờ nó muốn filter dựa trên published posts thôi, nên dùng cái này, là 1 cái custom manager
    # chỗ này có nghĩa, khi query postobjects thì trả về những posts có status là published
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    # chỗ này mặc định là các bài post sẽ được để vào category là 1, mà database chưa có category, nên mình phải tạo
    # vào admin dashboard để tạo

    # có protect, thì ai xoá cái category ở bảng category thì sẽ bảo vệ ở bảng POST
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    # nếu mà delete user thì sẽ xoá bài post của user đó lun
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)
        # sắp xếp post theo thứ tự tăng dần hay giảm dần by published ( là cái ngày_
    def __str__(self):
        return self.title