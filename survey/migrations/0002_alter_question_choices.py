# Generated by Django 3.2.6 on 2021-08-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(related_name='choices', to='survey.Choice'),
        ),
    ]