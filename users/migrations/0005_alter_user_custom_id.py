# Generated by Django 5.1.3 on 2025-03-11 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='custom_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
