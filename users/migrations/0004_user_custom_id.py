# Generated by Django 5.1.3 on 2025-03-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='custom_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
