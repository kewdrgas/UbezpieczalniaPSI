# Generated by Django 3.2.9 on 2022-02-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubezpieczenia', '0010_ubezpieczenie_kategoria_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (4, 'Elektronika'), (1, 'Samochód'), (3, 'Zdrowotne'), (2, 'Dom')], default=0),
        ),
        migrations.CreateModel(
            name='Zamowienia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=32)),
                ('nazwisko', models.CharField(max_length=32)),
                ('dodadkowy_opis', models.TextField(default='')),
                ('dane_kontaktowe', models.TextField(default='')),
                ('ubezpieczenie', models.ManyToManyField(related_name='Zamowienia', to='ubezpieczenia.Ubezpieczenie')),
            ],
        ),
    ]
