# Generated by Django 4.1.7 on 2023-02-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_timestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('action', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
            ],
        ),
    ]
