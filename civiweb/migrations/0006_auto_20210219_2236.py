# Generated by Django 3.1.6 on 2021-02-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civiweb', '0005_auto_20210219_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contactName',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
