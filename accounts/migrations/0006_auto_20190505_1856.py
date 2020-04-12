# Generated by Django 2.2.1 on 2019-05-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190505_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-datePosted']},
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set(),
        ),
    ]