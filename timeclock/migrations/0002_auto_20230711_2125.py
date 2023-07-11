# Generated by Django 3.2.20 on 2023-07-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeclock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(unique=True),
        ),
    ]