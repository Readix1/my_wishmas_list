from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid
from users.models import CustomUser  # Assuming you have a custom user model in users app


class Liste(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='listes'
    )
    is_shared = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    share_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.name} ({self.owner.email})"
    
    


class Produit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    liste = models.ForeignKey(
        Liste, 
        on_delete=models.CASCADE, 
        related_name='produits'
    )
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produits_ajoutes'
    )
    is_reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produits_reserves'
    )
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ShareRequest(models.Model):
    liste = models.ForeignKey(Liste, related_name='demandes', on_delete=models.CASCADE)
    follower  = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[
        ('pending', 'En attente'),
        ('accepted', 'Acceptée'),
        ('refused', 'Refusée'),
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('liste', 'follower')
