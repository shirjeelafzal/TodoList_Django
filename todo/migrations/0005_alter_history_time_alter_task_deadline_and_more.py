# Generated by Django 4.2.7 on 2023-11-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
