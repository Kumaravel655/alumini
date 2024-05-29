# Generated by Django 5.0 on 2024-05-19 16:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_skills_stud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('[+-/%@$^&*()!:;]', inverse_match=True)]),
        ),
    ]