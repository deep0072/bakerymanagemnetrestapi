# Generated by Django 3.0.1 on 2020-11-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='name',
            field=models.CharField(default='enter dish name', max_length=200),
        ),
    ]