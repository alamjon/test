# Generated by Django 3.0.7 on 2020-10-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201017_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='full_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='products',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='data',
            name='summ',
            field=models.CharField(default=None, max_length=90),
        ),
        migrations.AlterField(
            model_name='data',
            name='tel',
            field=models.CharField(default=None, max_length=13),
        ),
    ]