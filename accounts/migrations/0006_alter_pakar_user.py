# Generated by Django 4.2.13 on 2024-06-15 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_bidangkepakaran_pakar_userprofile_riwayatpenelitian_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pakar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
