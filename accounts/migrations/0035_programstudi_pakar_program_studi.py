# Generated by Django 4.2.13 on 2024-06-26 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_remove_pakar_minat_penelitian_pakar_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramStudi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='pakar',
            name='program_studi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pakar', to='accounts.programstudi'),
            preserve_default=False,
        ),
    ]