# Generated by Django 4.2.4 on 2023-08-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_setting_phone2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.TextField(max_length=240),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
