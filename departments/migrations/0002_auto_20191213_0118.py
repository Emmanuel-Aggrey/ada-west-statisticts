# Generated by Django 2.2.3 on 2019-12-13 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseline',
            name='activity',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='baseline',
            name='value',
            field=models.PositiveIntegerField(blank=True, help_text='numbers only', null=True),
        ),
    ]