# Generated by Django 2.2.1 on 2019-06-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('esalary', models.IntegerField()),
                ('ecity', models.CharField(max_length=30)),
            ],
        ),
    ]
