# Generated by Django 3.1.7 on 2021-06-01 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ganaderia', '0008_auto_20210601_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ternero',
            name='madre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Madre', to='ganaderia.vacamadre'),
        ),
    ]
