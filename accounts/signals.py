# accounts/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User  # Adjust this import based on your project structure
from .models import Pakar  # Adjust this import based on your project structure

# Buat sinyal post_save untuk membuat Pakar setiap kali User baru disimpan
@receiver(post_save, sender=User)
def create_user_pakar(sender, instance, created, **kwargs):
    if created:
        Pakar.objects.create(user=instance)
