# Generated by Django 2.0.2 on 2018-02-28 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0002_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mustbuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
        ),
    ]
