# Generated by Django 4.1 on 2024-04-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_photo',
            field=models.FileField(default='default_cover.jpg', upload_to='post_covers/'),
        ),
    ]
