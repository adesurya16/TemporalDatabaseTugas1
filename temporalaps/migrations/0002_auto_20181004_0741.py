# Generated by Django 2.1.1 on 2018-10-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temporalaps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='Valid_time_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='Valid_time_start',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='anggota',
            name='Alamat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='anggota',
            name='Telepon',
            field=models.CharField(max_length=255, null=True),
        ),
    ]