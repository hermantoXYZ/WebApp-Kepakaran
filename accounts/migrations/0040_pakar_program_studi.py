# Generated by Django 4.2.13 on 2024-06-27 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_programstudi'),
    ]

    operations = [
        migrations.AddField(
            model_name='pakar',
            name='program_studi',
            field=models.ManyToManyField(related_name='pakar', to='accounts.programstudi'),
        ),
    ]
