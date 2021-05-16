# Generated by Django 2.2.13 on 2021-05-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_roommodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='room_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]