# Generated by Django 4.1.11 on 2023-10-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis_ontology', '0009_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='kind',
            field=models.CharField(blank=True, choices=[(1, 'Place description ÖBL'), (2, 'ÖBL Haupttext'), (3, 'ÖBL Kurzinfo'), (4, 'Place review comments'), (5, 'Commentary Staribacher'), (6, 'Online Edition Haupttext'), (7, 'Nachrecherche'), (8, 'Soziale Herkunft'), (9, 'Verwandtschaft'), (10, 'Ausbildung / Studium / Studienreisen und diesbezügliche Ortsangaben'), (11, 'Berufstätigkeit / Lebensstationen und geographische Lebensmittelpunkte'), (12, 'Mitgliedschaften, Orden, Auszeichnungen und diesbezügliche Ortsangaben'), (13, 'Literatur'), (14, 'Beruf(e)'), (15, 'Sterbedatum'), (16, 'Adelsprädikat'), (17, 'Übersiedlung, Emigration, Remigration'), (18, 'Weitere Namensformen'), (19, 'Geburtsdatum'), (20, 'Sterbeort'), (21, 'Geburtsort'), (22, 'Religion(en)'), (23, 'Name'), (24, 'Übersiedlungen, Emigration, Remigration'), (25, 'Pseudonyme'), (26, 'Soziale Herkunft'), (27, 'ÖBL Werkverzeichnis')], max_length=255, null=True),
        ),
    ]