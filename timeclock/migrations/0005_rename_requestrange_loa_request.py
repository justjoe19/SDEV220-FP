# Generated by Django 3.2.20 on 2023-07-28 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeclock', '0004_rename_request_loa_requestrange'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loa',
            old_name='requestRange',
            new_name='request',
        ),
    ]
