# Generated by Django 3.0.2 on 2020-02-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200202_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
