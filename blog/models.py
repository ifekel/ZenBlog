from django.db import models
import uuid


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    title = models.CharField(max_length=500)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:30]


class BlogImage(models.Model):
    image = models.ImageField(upload_to="blog_photos/")
    blog = models.ForeignKey(
        Blog, related_name="blog_images", on_delete=models.CASCADE)
