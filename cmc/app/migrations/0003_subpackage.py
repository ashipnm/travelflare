# Generated by Django 5.0 on 2024-01-06 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_packages'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_place_image', models.ImageField(upload_to='subpackage_images/')),
                ('sub_place_name', models.CharField(max_length=255)),
                ('sub_description', models.TextField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.packages')),
            ],
        ),
    ]
