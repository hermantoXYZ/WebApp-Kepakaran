# Generated by Django 4.2.13 on 2024-07-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0043_alter_pakar_program_studi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='/media/assets/default.jpg', upload_to='profile_pics'),
        ),
    ]
