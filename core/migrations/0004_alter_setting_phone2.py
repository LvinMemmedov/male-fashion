# Generated by Django 4.2.4 on 2023-08-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_new_category_new_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='phone2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
