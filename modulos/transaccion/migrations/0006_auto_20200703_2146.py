# Generated by Django 3.0.8 on 2020-07-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0005_auto_20200703_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='transaction_amount',
            field=models.PositiveIntegerField(null=True, verbose_name='Monto'),
        ),
    ]
