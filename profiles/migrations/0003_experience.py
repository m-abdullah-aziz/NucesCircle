# Generated by Django 2.2 on 2019-04-26 20:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20190424_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expNo', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('company', models.CharField(blank=True, max_length=10, null=True)),
                ('fromDate', models.DateField(default=datetime.date.today)),
                ('toDate', models.DateField(default=datetime.date.today)),
                ('explanation', models.CharField(blank=True, max_length=10, null=True)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user1', 'expNo')},
            },
        ),
    ]