# Generated by Django 3.1.7 on 2021-05-31 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ganaderia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacamadre',
            name='id_animal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ganaderia.animal'),
            preserve_default=False,
        ),
    ]