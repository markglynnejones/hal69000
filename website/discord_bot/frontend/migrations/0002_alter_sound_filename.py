# Generated by Django 4.0.1 on 2022-01-17 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='filename',
            field=models.FileField(max_length=30, upload_to=''),
        ),
    ]
