# Generated by Django 2.0.5 on 2020-01-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200120_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='householddata',
            name='image_thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='thumbs'),
        ),
    ]
