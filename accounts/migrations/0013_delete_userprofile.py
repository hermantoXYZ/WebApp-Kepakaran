# Generated by Django 4.2.13 on 2024-06-16 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_userprofile_delete_socialmedia'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]