# Generated by Django 3.2 on 2021-06-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0004_remove_dreamjob_skills_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='dreamjob',
            name='skills_pic',
            field=models.ImageField(blank=True, upload_to=None),
        ),
    ]