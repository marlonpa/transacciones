from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.db.models import SET_NULL, ForeignKey


class Archivo(models.Model):
    name = models.FileField(verbose_name='Name', max_length=250)
    fecha = models.DateField(null=True, blank=True)

    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='User',
        null=True,
        on_delete=SET_NULL)

    def __str__(self):
        return '{},{},{}'.format(self.name, self.fecha, self.user)


class Transaccion(models.Model):
    transaction_id = models.CharField(verbose_name='Name', max_length=250)
    transaction_date = models.CharField(verbose_name='Date', max_length=250, null=True)
    transaction_amount = models.CharField(verbose_name='Monto', max_length=250, null=True)
    client_id = models.CharField(verbose_name='Id cliente', max_length=250, null=True)
    client_name = models.CharField(verbose_name='client_name', max_length=100)
    archivo = ForeignKey(
        Archivo,
        verbose_name='User',
        null=True,
        on_delete=SET_NULL)

    def __str__(self):
        return '{},{},{},{},{}'.format(self.transaction_id, self.transaction_date, self.transaction_date,
                                       self.client_id, self.client_name)





