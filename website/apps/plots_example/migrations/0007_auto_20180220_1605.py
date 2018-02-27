# Generated by Django 2.0.1 on 2018-02-20 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots_example', '0006_auto_20180207_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagedata',
            options={'verbose_name_plural': 'image data'},
        ),
        migrations.AlterField(
            model_name='imagedata',
            name='inst',
            field=models.CharField(choices=[('FGS', 'FGS'), ('MIRI', 'MIRI'), ('NIRCam', 'NIRCam'), ('NIRISS', 'NIRISS'), ('NIRSpec', 'NIRSpec')], default=None, max_length=6, verbose_name='instrument'),
        ),
    ]