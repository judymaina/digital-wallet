# Generated by Django 4.0.6 on 2022-07-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(max_length=20)),
                ('balance', models.IntegerField()),
                ('account_name', models.CharField(max_length=20)),
            ],
        ),
    ]
