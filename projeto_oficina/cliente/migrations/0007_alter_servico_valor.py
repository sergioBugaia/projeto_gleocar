# Generated by Django 4.1.2 on 2023-02-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_alter_cliente_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='valor'),
        ),
    ]