# Generated by Django 4.1.2 on 2023-01-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_alter_servico_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cliente_email',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_telefone',
            field=models.CharField(default=0, max_length=11),
        ),
    ]
