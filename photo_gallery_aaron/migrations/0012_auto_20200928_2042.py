# Generated by Django 3.1.1 on 2020-09-28 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo_gallery_aaron', '0011_auto_20200924_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo_comments', to='photo_gallery_aaron.photo'),
        ),
    ]
