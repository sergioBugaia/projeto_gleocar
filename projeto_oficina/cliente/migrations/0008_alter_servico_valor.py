# Generated by Django 4.1.2 on 2023-02-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_alter_servico_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.CharField(max_length=12),
        ),
    ]