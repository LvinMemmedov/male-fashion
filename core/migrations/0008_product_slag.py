# Generated by Django 4.2.4 on 2023-08-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_setting_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slag',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
