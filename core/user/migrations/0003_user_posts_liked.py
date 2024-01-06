# Generated by Django 4.2 on 2024-01-06 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0002_alter_post_created_alter_post_updated'),
        ('core_user', '0002_alter_user_created_alter_user_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.post'),
        ),
    ]