# Generated by Django 3.0 on 2020-09-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_householddata_risk_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householddata',
            name='risk_score',
            field=models.IntegerField(default=0),
        ),
    ]
