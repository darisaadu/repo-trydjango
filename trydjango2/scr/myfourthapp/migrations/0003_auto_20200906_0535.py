# Generated by Django 2.0.7 on 2020-09-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfourthapp', '0002_auto_20200906_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproduct',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]