# Generated by Django 4.2.13 on 2024-06-26 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_programstudi_pakar_program_studi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pakar',
            old_name='program_studi',
            new_name='prodi',
        ),
    ]
