# Generated by Django 3.1.5 on 2021-02-02 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210201_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='color',
            field=models.CharField(max_length=20),
        ),
    ]