from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name',)

    # Slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class PostItem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    post_image = models.ImageField(
        upload_to='uploads', blank=True, null=True, default='default.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_post = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'List Item'

    # slug
    def save(self, *args, **kwargs):
        self.slug = slugify('title')
        super(PostItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
