# Generated by Django 4.2.13 on 2024-06-26 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_rename_program_studi_pakar_prodi'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProgramStudi',
            new_name='Prodi',
        ),
    ]
