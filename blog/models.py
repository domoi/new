from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    photo = models.ImageField(upload_to='', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,verbose_name='Категория')
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.full = self.title
        self.slug = slugify(self.full)
        super(News, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('blog', args=[self.slug])


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="", null=True,blank=True)

    def __str__(self):
        return self.title

