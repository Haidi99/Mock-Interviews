# Generated by Django 3.2 on 2021-06-06 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0005_dreamjob_skills_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dreamjob',
            name='skills_pic',
        ),
    ]