# Generated by Django 2.2.4 on 2021-04-02 17:03

from django.db import migrations


def generate_standartized_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber = flat.owners_phonenumber.\
            replace('(', '').\
            replace(')', '').\
            replace(' ', '').\
            replace('-', '')
        if str(phonenumber).startswith('8'):
            phonenumber = f'+7{str(phonenumber)[1:]}'
        flat.owner_standartized_phonenumber = phonenumber
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20210402_1955'),
    ]

    operations = [
        migrations.RunPython(generate_standartized_phonenumbers)
    ]
