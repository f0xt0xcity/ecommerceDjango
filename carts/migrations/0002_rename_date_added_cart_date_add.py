# Generated by Django 3.2.9 on 2021-11-12 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='date_added',
            new_name='date_add',
        ),
    ]
