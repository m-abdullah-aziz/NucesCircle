# Generated by Django 2.2 on 2019-04-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]