# Generated by Django 4.0.2 on 2022-02-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubezpieczenia', '0008_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Elektronika'), (2, 'Dom'), (3, 'Zdrowotne'), (1, 'Samochód'), (0, 'Inne')], default=0),
        ),
    ]
