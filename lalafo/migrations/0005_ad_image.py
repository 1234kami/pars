# Generated by Django 3.2.12 on 2023-10-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lalafo', '0004_auto_20231031_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
    ]