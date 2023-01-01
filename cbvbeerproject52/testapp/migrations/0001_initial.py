# Generated by Django 3.2.4 on 2022-10-27 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=30)),
                ('taste', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]
