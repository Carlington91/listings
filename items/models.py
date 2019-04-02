from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    description = models.TextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)


class PostItem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    post_image = models.ImageField(
        upload_to='uploads', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_post = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
