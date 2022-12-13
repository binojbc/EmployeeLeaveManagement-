# Generated by Django 4.1.3 on 2022-12-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=200)),
                ('FullName', models.CharField(max_length=200)),
                ('IsSuperUser', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=200)),
                ('Designation', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=255)),
            ],
        ),
    ]