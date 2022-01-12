# Generated by Django 3.2.9 on 2021-12-01 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teamlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('no_of_members', models.IntegerField(default=1)),
                ('team_type', models.CharField(max_length=200)),
            ],
        ),
    ]
