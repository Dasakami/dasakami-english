# Generated by Django 5.1.3 on 2025-03-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_remove_card_description_alter_card_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idiom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idiom', models.CharField(max_length=255)),
                ('meaning', models.TextField()),
                ('usage', models.TextField()),
            ],
        ),
    ]
