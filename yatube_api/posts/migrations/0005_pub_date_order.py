# Generated by Django 2.2.16 on 2022-07-25 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_changed_follow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pub_date'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
