# Generated by Django 2.0.7 on 2020-10-23 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='content'),
        ),
        migrations.AddField(
            model_name='article',
            name='reporter',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Reporter'),
            preserve_default=False,
        ),
    ]
