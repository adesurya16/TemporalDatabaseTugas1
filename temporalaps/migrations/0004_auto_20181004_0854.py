# Generated by Django 2.1.1 on 2018-10-04 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temporalaps', '0003_auto_20181004_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anggota',
            name='Divisi',
            field=models.CharField(max_length=255),
        ),
    ]