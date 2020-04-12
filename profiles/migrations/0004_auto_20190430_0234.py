# Generated by Django 2.2 on 2019-04-29 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='explanation',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]