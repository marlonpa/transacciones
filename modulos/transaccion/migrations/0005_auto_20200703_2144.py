# Generated by Django 3.0.8 on 2020-07-04 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaccion', '0004_auto_20200703_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='transaction_date',
            field=models.CharField(max_length=250, null=True, verbose_name='Date'),
        ),
    ]
