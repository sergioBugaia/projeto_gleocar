# Generated by Django 4.1.2 on 2023-02-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_alter_cliente_cliente_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cliente_telefone',
            field=models.CharField(max_length=13),
        ),
    ]
