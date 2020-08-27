from hashlib import md5

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Creado en')
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Actualizado en')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Creado por')

    class Meta:
        abstract = True


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Apellidos')
    email = models.EmailField(blank=False, unique=True)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
