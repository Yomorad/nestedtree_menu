# Generated by Django 5.1.1 on 2024-10-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
