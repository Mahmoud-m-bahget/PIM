# Generated by Django 3.1.7 on 2021-03-22 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Code', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=250)),
                ('Price', models.FloatField()),
                ('Quantity', models.FloatField()),
                ('Start_Date', models.DateTimeField()),
                ('Dration', models.CharField(choices=[('5 days,', '5 days,'), ('10 days', '10 days'), ('15 days', '15 days'), ('20 days', '20 days')], max_length=250)),
                ('Image', models.ImageField(blank=True, upload_to='static/img')),
                ('State', models.CharField(choices=[('Active', 'Active'), ('Ended', 'Ended')], max_length=250)),
                ('category', models.ManyToManyField(to='Category.Categories')),
            ],
        ),
    ]
