# Generated by Django 4.2 on 2023-05-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='products',
            name='pages',
            field=models.IntegerField(),
        ),
    ]
