# Generated by Django 3.0.7 on 2020-08-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200817_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='summ',
            field=models.CharField(max_length=900000),
        ),
    ]