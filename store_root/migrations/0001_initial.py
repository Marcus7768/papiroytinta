# Generated by Django 4.2 on 2023-05-14 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Root',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=150)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
    ]
