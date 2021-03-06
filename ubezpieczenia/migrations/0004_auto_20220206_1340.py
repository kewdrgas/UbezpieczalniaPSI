# Generated by Django 3.2.9 on 2022-02-06 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubezpieczenia', '0003_auto_20220206_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubezpieczenie',
            name='dodatkowe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ubezpieczenia.dodatkoweinfo'),
        ),
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Zdrowotne'), (4, 'Elektronika'), (1, 'Samochód'), (0, 'Inne'), (2, 'Dom')], default=0),
        ),
    ]
