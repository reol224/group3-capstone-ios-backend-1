# Generated by Django 3.2.9 on 2022-08-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photos_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
