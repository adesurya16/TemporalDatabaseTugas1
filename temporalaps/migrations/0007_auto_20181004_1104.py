# Generated by Django 2.1.1 on 2018-10-04 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temporalaps', '0006_auto_20181004_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]