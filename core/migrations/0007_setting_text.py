# Generated by Django 4.2.4 on 2023-08-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
