# Generated by Django 3.1.3 on 2020-11-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_ransomwaresadd'),
    ]

    operations = [
        migrations.AddField(
            model_name='ransomwares',
            name='url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
