# Generated by Django 2.0.7 on 2020-09-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('summary', models.CharField(max_length=120)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
