# Generated by Django 4.1.4 on 2022-12-25 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakar',
            name='number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
