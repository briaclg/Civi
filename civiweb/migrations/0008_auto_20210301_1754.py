# Generated by Django 3.1.6 on 2021-03-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civiweb', '0007_auto_20210301_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='candidateCounter',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='creationDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='durationBroadcast',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='missionDescription',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='missionEndDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='missionStartDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='missionType',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='missionTypeEn',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='startBroadcastDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='viewCounter',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
