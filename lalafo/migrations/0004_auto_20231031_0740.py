# Generated by Django 3.2.12 on 2023-10-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lalafo', '0003_lalafoitemimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='lalafoitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images/'),
        ),
        migrations.DeleteModel(
            name='LalafoItemImages',
        ),
    ]
