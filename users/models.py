from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    #Level -> 0:Usuario comum, 1: Dono de loja, 2:admin
    level = models.DecimalField(max_digits=2, max_length=1, decimal_places=0, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        # Define como irá aparecer em formularios e no admin
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

        # Ordena de forma alfabetica (para inverso colocar -)
        ordering = ['email']


    def __str__(self):
        return self.email