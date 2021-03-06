# Generated by Django 3.2.7 on 2021-10-26 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plug',
            fields=[
                ('hash', models.PositiveBigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('description', models.TextField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='PlugSet',
            fields=[
                ('hash', models.PositiveBigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('reusable_plug_items', models.ManyToManyField(editable=False, to='api.Plug')),
            ],
        ),
        migrations.CreateModel(
            name='WishlistWeapon',
            fields=[
                ('hash', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=100)),
                ('vanguard', models.JSONField(blank=True, null=True)),
                ('crucible', models.JSONField(blank=True, null=True)),
                ('gambit', models.JSONField(blank=True, null=True)),
                ('junk', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaticWeapon',
            fields=[
                ('hash', models.PositiveBigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=100)),
                ('icon', models.CharField(editable=False, max_length=100)),
                ('flavor_text', models.TextField(editable=False)),
                ('tier_type', models.CharField(editable=False, max_length=10)),
                ('weapon_type', models.CharField(editable=False, max_length=30)),
                ('slot_type', models.CharField(editable=False, max_length=7)),
                ('ammo_type', models.CharField(editable=False, max_length=7)),
                ('damage_type', models.CharField(editable=False, max_length=7)),
                ('watermark_icons', models.JSONField()),
                ('index', models.PositiveBigIntegerField(editable=False)),
                ('is_sunset', models.BooleanField(default=False)),
                ('column_four_hash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='column_four', to='api.plugset')),
                ('column_one_hash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='column_one', to='api.plugset')),
                ('column_three_hash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='column_three', to='api.plugset')),
                ('column_two_hash', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='column_two', to='api.plugset')),
            ],
        ),
    ]
