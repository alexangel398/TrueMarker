# Generated by Django 4.2.4 on 2023-10-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_remove_user_avatar_remove_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='superuser'),
        ),
    ]