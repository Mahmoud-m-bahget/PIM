# Generated by Django 3.1.7 on 2021-03-22 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20210322_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Start_Date',
            field=models.DateTimeField(blank=True),
        ),
    ]
