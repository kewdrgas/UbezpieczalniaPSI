# Generated by Django 3.2.9 on 2022-02-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubezpieczenia', '0005_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (2, 'Dom'), (1, 'Samochód'), (3, 'Zdrowotne'), (4, 'Elektronika')], default=0),
        ),
    ]
