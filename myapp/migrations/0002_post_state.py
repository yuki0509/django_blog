# Generated by Django 3.0.4 on 2021-02-01 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.IntegerField(default=1),
        ),
    ]