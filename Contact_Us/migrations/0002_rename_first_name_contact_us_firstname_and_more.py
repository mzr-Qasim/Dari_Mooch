# Generated by Django 5.0.6 on 2024-07-02 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contact_Us', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_us',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='contact_us',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='contact_us',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
