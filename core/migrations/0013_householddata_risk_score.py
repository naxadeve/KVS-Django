# Generated by Django 3.0 on 2020-09-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_householddata_flood_resilience_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='householddata',
            name='risk_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
