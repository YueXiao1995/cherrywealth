# Generated by Django 3.0.3 on 2021-09-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('wealth', models.CharField(max_length=200)),
                ('brief_intro', models.TextField()),
            ],
        ),
    ]
