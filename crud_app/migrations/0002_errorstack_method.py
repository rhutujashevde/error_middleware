# Generated by Django 3.0.4 on 2020-03-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorstack',
            name='method',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
