# Generated by Django 4.2.13 on 2024-06-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='scopus_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sinta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
