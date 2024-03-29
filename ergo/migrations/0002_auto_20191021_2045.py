# Generated by Django 2.2.2 on 2019-10-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ergo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ergometria',
            name='carga',
            field=models.CharField(max_length=150, null=True, verbose_name='Carga'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='motivo_suspencion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='percent_fcmp',
            field=models.FloatField(null=True, verbose_name='Percent fcmp'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='sintomas',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='st',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='st_mm',
            field=models.FloatField(null=True, verbose_name='St mm'),
        ),
        migrations.AlterField(
            model_name='ergometria',
            name='ta_plana',
            field=models.CharField(default=False, max_length=150),
        ),
    ]
