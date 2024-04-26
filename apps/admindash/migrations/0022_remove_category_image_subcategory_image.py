# Generated by Django 4.2 on 2024-04-26 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindash', '0021_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subcategory'),
        ),
    ]
