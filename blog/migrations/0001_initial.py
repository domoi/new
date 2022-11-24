# Generated by Django 4.1.3 on 2022-11-04 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Контент')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('slug', models.SlugField(default='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Категория')),
            ],
        ),
    ]