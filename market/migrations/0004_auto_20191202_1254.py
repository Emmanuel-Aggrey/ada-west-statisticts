# Generated by Django 2.2.3 on 2019-12-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20191202_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='market_name',
            field=models.CharField(max_length=200),
        ),
    ]
