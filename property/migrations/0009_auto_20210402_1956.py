# Generated by Django 2.2.4 on 2021-04-02 17:03

from django.db import migrations
import phonenumbers


def generate_standartized_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phonenumber):
            phonenumber = phonenumbers.format_number(
                phonenumber,
                phonenumbers.PhoneNumberFormat.E164
            )
        else:
            phonenumber = None
        flat.owner_standartized_phonenumber = phonenumber
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20210402_1955'),
    ]

    operations = [
        migrations.RunPython(generate_standartized_phonenumbers)
    ]
