# Generated by Django 2.0.6 on 2020-02-26 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]