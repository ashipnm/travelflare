# Generated by Django 5.0 on 2024-01-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_image', models.ImageField(upload_to='package_images/')),
                ('place_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
