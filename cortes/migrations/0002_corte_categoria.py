# Generated by Django 4.0.2 on 2022-02-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cortes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='corte',
            name='categoria',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
