# Generated by Django 2.2.3 on 2019-07-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20190726_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
