# Generated by Django 4.2.4 on 2023-09-01 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
