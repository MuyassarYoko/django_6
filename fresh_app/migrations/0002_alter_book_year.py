# Generated by Django 5.1.1 on 2024-09-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.DateField(),
        ),
    ]
