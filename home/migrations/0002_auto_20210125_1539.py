# Generated by Django 3.1.4 on 2021-01-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='person',
        ),
        migrations.AddField(
            model_name='car',
            name='person',
            field=models.ManyToManyField(to='home.Person'),
        ),
    ]