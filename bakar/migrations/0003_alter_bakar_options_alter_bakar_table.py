# Generated by Django 4.1.4 on 2022-12-25 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakar', '0002_alter_bakar_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bakar',
            options={'ordering': ('number',), 'verbose_name': 'Öğrenci', 'verbose_name_plural': 'Öğrenciler'},
        ),
        migrations.AlterModelTable(
            name='bakar',
            table='bakarlar',
        ),
    ]