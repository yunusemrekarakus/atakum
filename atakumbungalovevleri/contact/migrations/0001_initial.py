# Generated by Django 4.1.5 on 2023-02-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_soyad', models.CharField(max_length=50, verbose_name='AD SOYAD')),
                ('email', models.EmailField(max_length=30, verbose_name='EMAİL')),
                ('phone', models.CharField(max_length=15, verbose_name='TEL NO')),
                ('message', models.TextField()),
            ],
        ),
    ]
