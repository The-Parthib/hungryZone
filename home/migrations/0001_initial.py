# Generated by Django 5.0.7 on 2024-07-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.CharField(max_length=125)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]