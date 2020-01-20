# Generated by Django 2.2.3 on 2019-11-27 09:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('unit_of_sale', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Commodity',
                'verbose_name_plural': "Commodity's",
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='create a new market', max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Market',
                'verbose_name_plural': 'Market',
                'ordering': ['-date_add'],
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('market_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='market.Market')),
            ],
            options={
                'ordering': ['-date_add'],
            },
        ),
        migrations.CreateModel(
            name='Commodity_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, help_text='eg if you select rice as commodity local or perfume will be the commodity type', max_length=200, null=True, verbose_name='commodity type')),
                ('num_pieces', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='number of pieces')),
                ('weight_volume', models.CharField(blank=True, max_length=5, null=True, verbose_name='weight volume (kg/litre)')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='price (GH₵)')),
                ('trader', models.CharField(blank=True, choices=[('t1', 'Trader 1'), ('t2', 'Trader 2'), ('t3', 'Trader 3'), ('t4', 'Trader 4'), ('t5', 'Trader 5')], max_length=2, null=True)),
                ('commodity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodities', to='market.Commodity', verbose_name='commodity')),
                ('visit_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_visits', to='market.Visit')),
            ],
            options={
                'verbose_name': 'Commodity',
                'verbose_name_plural': "Commodity Type's",
            },
        ),
    ]