# Generated by Django 3.0 on 2021-07-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etiqette', '0004_session_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='num_of_seats',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
