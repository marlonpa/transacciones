from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Users(AbstractUser):
    is_admin = models.BooleanField(default=False, verbose_name='Administrador')
    ide = models.CharField(verbose_name='Identificacion', max_length=14, null=True, blank=True)
    celular = models.CharField(
        max_length=10, verbose_name='Celular', null=True, blank=True,
        validators=[RegexValidator('^3[0-9]{9}$', '3XXXXXXXXX ejemplo', 'Entrada invalida')]
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        ordering = ['ide']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.get_full_name()}'
