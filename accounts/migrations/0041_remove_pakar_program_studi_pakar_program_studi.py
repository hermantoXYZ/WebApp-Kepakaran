# Generated by Django 4.2.13 on 2024-06-27 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_pakar_program_studi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pakar',
            name='program_studi',
        ),
        migrations.AddField(
            model_name='pakar',
            name='program_studi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pakar', to='accounts.programstudi'),
            preserve_default=False,
        ),
    ]
