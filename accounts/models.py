# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime
import os
import random
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

def rename_image(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    
    current_date = datetime.now().strftime('%Y_%m_%d')
    random_number = random.randint(100000, 999999)  # Generate a 6-digit random number
    
    if hasattr(instance, 'judul') and instance.judul:
        filename = f"{slugify(instance.judul)}_{current_date}_{random_number}.{ext}"
    elif hasattr(instance, 'title') and instance.title:
        filename = f"{slugify(instance.title)}_{current_date}_{random_number}.{ext}"
    elif instance.pk:
        filename = f"{instance.pk}_{current_date}_{random_number}.{ext}"
    else:
        filename = f"{current_date}_{random_number}.{ext}"
    
    return os.path.join(upload_to, filename)

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_dosen = models.BooleanField('Is dosen', default=False)
    is_user = models.BooleanField('Is user', default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    scopus_id = models.CharField(max_length=100, blank=True, null=True)
    sinta = models.CharField(max_length=100, blank=True, null=True)
    google_scholar = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
    

    
class Page (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to=rename_image, null=True, blank=True)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Category)
def create_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        
class PostNews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    images = models.ImageField(upload_to=rename_image, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title

@receiver(pre_save, sender=PostNews)
def pre_save_postnews_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    

class BidangKepakaran(models.Model):
    nama_bidang = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama_bidang)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama_bidang
    
    def get_users(self):
        return [pakar.user for pakar in self.pakar.all()]
    
    

class Pakar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bidang_kepakaran = models.ManyToManyField(BidangKepakaran, related_name='pakar')
    tags = TaggableManager()
    

    def __str__(self):
        return self.user.username

class Pendidikan(models.Model):
    pakar = models.ForeignKey(Pakar, on_delete=models.CASCADE, related_name='pendidikan')
    pendidikan = models.CharField(max_length=100)
    tahun = models.IntegerField()
    program_studi = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pakar.user.username} - {self.pendidikan}"

# class Publikasi(models.Model):
#     pakar = models.ForeignKey(Pakar, on_delete=models.CASCADE, related_name='publikasi')
#     judul_publikasi = models.CharField(max_length=200)
#     tahun_publikasi = models.IntegerField()
#     link_publikasi = models.URLField()
#     tim_publikasi = models.CharField(max_length=200)

#     def __str__(self):
#         return self.judul_publikasi

CATEGORY_CHOICES = (
    ('nasional', 'Nasional'),
    ('Internasional', 'Internasional'),
)

class Penelitian(models.Model):
    pakar = models.ForeignKey(Pakar, on_delete=models.CASCADE, related_name='penelitian')
    judul_penelitian = models.CharField(max_length=200)
    tahun_penelitian = models.IntegerField(blank=True, null=True)
    link_penelitian = models.URLField(blank=True, null=True)
    tim_penelitian = models.CharField(max_length=200, blank=True, null=True)
    category_penelitian = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.judul_penelitian

# class RiwayatPenelitian(models.Model):
#     pakar = models.ForeignKey(Pakar, on_delete=models.CASCADE, related_name='riwayat_penelitian')
#     judul_riwayat = models.CharField(max_length=200)
#     tahun_riwayat = models.IntegerField()
#     link_riwayat_penelitian = models.URLField()
#     tim_riwayat = models.CharField(max_length=200)

#     def __str__(self):
#         return self.judul_riwayat

class InTheNews(models.Model):
    pakar = models.ForeignKey(Pakar, on_delete=models.CASCADE, related_name='the_news')
    judul_news = models.CharField(max_length=200)
    tanggal_terbit = models.DateField()
    link_news = models.URLField()
    media = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=rename_image, null=True, blank=True)

    def __str__(self):
        return self.judul_news
    


class Pengabdian(models.Model):
    pakar = models.ForeignKey(Pakar, on_delete=models.CASCADE, related_name='pengabdian')
    judul_pengabdian = models.CharField(max_length=200, blank=True, null=True)
    tahun_pengabdian = models.IntegerField(blank=True, null=True)
    link_pengabdian = models.URLField(blank=True, null=True)
    tim_pengabdian = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.judul_pengabdian
    
class Book (models.Model):
    pakar = models.ForeignKey(Pakar, on_delete=models.CASCADE, related_name='book')
    judul_book = models.CharField(max_length=200, blank=True, null=True)
    tahun_book = models.IntegerField(blank=True, null=True)
    link_book = models.URLField(blank=True, null=True)
    penerbit = models.CharField(max_length=200, blank=True, null=True)
    cover_book = models.ImageField(upload_to=rename_image, null=True, blank=True)

    def __str__(self):
        return self.judul_book
    

class Organisasi(models.Model):
    pakar = models.ForeignKey(Pakar, on_delete=models.CASCADE, related_name='organisasi')
    nama_organisasi = models.CharField(max_length=200, blank=True, null=True)
    tahun_organisasi = models.IntegerField(blank=True, null=True)
    jabatan_organisasi = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nama_organisasi
    

