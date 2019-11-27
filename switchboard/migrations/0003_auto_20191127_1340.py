# Generated by Django 2.2.7 on 2019-11-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switchboard', '0002_searchquery_credentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='api_version',
            field=models.IntegerField(choices=[(0, 'NA'), (1, 'Openskies_V1'), (2, 'Openskies_V2')], verbose_name='version'),
        ),
    ]
