# Generated by Django 3.0 on 2021-07-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etiqette', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='movie_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cinema',
            name='rating',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]