# Generated by Django 4.2.13 on 2024-06-25 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_pakar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='penerbit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]