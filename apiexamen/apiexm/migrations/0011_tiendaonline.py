# Generated by Django 2.1.3 on 2018-11-30 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiexm', '0010_tiendafisica'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiendaOnLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=255)),
                ('NombreSucursal', models.CharField(max_length=255)),
                ('Link', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
            ],
        ),
    ]