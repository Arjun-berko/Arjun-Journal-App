# Generated by Django 4.1.6 on 2023-03-04 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_picture_alter_profile_user_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
