# Generated by Django 3.0 on 2020-09-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0006_auto_20200903_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='map_to_field',
            new_name='map_to_field_1',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_types',
            field=models.CharField(choices=[('substring', 'answer should be derived from substring of the field data'), ('code_mapping', 'certain coding mechanism in the data, e.g. number codes mentioned in data for different answer options'), ('time_range_from_substring', 'time range need to be derived from substring of the field'), ('count_from_substring', 'count need to be derived from substring of the field'), ('complex_calculation', 'involves a number of factors ans fields to find the score')], default='substrings', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='map_to_field_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='scoring_method',
            field=models.CharField(choices=[('substrings', 'scoring based on a fixed number of substrings'), ('yes/no', 'scoring based on simple yes or no'), ('keywords', 'scoring based on a fixed number of keywords'), ('composite_count', 'options varries from No to More than 1'), ('multifield_substring', 'one that combines data from 2 or more fields based on substrings'), ('range_based', 'options have some kind of range of values, e.g. distance 50-100 metre, 100-200 metre')], default='substrings', max_length=200),
        ),
    ]
