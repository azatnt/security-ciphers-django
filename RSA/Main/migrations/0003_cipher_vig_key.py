# Generated by Django 3.1.5 on 2021-03-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_cipher_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='cipher',
            name='vig_key',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
