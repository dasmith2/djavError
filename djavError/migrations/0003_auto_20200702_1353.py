# Generated by Django 3.0.5 on 2020-07-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djavError', '0002_toomanyqueriesrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longrequest',
            name='total_duration',
            field=models.FloatField(help_text='In seconds.'),
        ),
    ]