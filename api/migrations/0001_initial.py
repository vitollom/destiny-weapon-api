# Generated by Django 3.2.7 on 2021-10-01 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticWeapon',
            fields=[
                ('hash', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('weapon_dict', models.JSONField()),
            ],
        ),
    ]