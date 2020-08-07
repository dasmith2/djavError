# Generated by Django 3.0.5 on 2020-07-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djavError', '0007_auto_20200710_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='fixed',
            field=models.DateTimeField(blank=True, help_text='When, if ever, was this problem fixed?', null=True),
        ),
        migrations.AlterField(
            model_name='longrequest',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='toomanyqueriesrequest',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]