# Generated by Django 2.0.6 on 2019-02-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('breed', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
    ]
