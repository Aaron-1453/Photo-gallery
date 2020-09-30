# Generated by Django 3.1.1 on 2020-09-29 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo_gallery_aaron', '0012_auto_20200928_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='photos',
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='photo_gallery_aaron.photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='photo_gallery_aaron.gallery'),
        ),
    ]