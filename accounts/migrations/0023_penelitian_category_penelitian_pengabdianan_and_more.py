# Generated by Django 4.2.13 on 2024-06-21 02:41

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_inthenews_tanggal_terbit'),
    ]

    operations = [
        migrations.AddField(
            model_name='penelitian',
            name='category_penelitian',
            field=models.CharField(choices=[('penelitian', 'Penelitian'), ('riwayat', 'Riwayat')], default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Pengabdianan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_pengabdian', models.CharField(max_length=200)),
                ('tahun_pengabdian', models.IntegerField()),
                ('link_pengabdian', models.URLField()),
                ('tim_pengabdian', models.CharField(max_length=200)),
                ('pakar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pengabdian', to='accounts.pakar')),
            ],
        ),
        migrations.CreateModel(
            name='Organisasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_organisasi', models.CharField(max_length=200)),
                ('tahun_organisasi', models.IntegerField()),
                ('jabatan_organisasi', models.CharField(max_length=200)),
                ('pakar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organisasi', to='accounts.pakar')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_book', models.CharField(max_length=200)),
                ('tahun_book', models.IntegerField()),
                ('link_book', models.URLField()),
                ('cover_book', models.ImageField(blank=True, null=True, upload_to=accounts.models.rename_image)),
                ('pakar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='accounts.pakar')),
            ],
        ),
    ]
