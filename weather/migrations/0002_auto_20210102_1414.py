# Generated by Django 3.1.4 on 2021-01-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название города'),
        ),
    ]
