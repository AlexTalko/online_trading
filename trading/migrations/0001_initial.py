# Generated by Django 5.1.1 on 2024-10-27 20:58

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время последнего изменения')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(max_length=100, verbose_name='улица')),
                ('house_number', models.CharField(max_length=100, verbose_name='номер дома')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время последнего изменения')),
                ('name', models.CharField(max_length=100, verbose_name='наименование')),
                ('model', models.CharField(max_length=100, verbose_name='модель')),
                ('release_date', models.DateField(help_text='ДД.ММ.ГГГГ', verbose_name='дата выпуска')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время последнего изменения')),
                ('name', models.CharField(max_length=100)),
                ('debt', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True, verbose_name='задолженность')),
                ('contacts', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='trading.contacts')),
                ('products', models.ManyToManyField(to='trading.products')),
            ],
            options={
                'verbose_name': 'производитель',
                'verbose_name_plural': 'производители',
            },
        ),
        migrations.CreateModel(
            name='RetailNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время последнего изменения')),
                ('name', models.CharField(max_length=100)),
                ('debt', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=15, null=True, verbose_name='задолженность')),
                ('contacts', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='retail_network', to='trading.contacts')),
                ('products', models.ManyToManyField(to='trading.products')),
                ('provider_factory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplied_retail_networks', to='trading.factory')),
            ],
            options={
                'verbose_name': 'розничная сеть',
                'verbose_name_plural': 'розничные сети',
            },
        ),
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время последнего изменения')),
                ('name', models.CharField(max_length=100)),
                ('debt', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=15, verbose_name='задолженность')),
                ('contacts', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trader', to='trading.contacts')),
                ('products', models.ManyToManyField(to='trading.products')),
                ('provider_factory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provider_for_traders', to='trading.factory')),
                ('provider_retail_network', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provider_for_traders', to='trading.retailnetwork')),
            ],
            options={
                'verbose_name': 'индивидуальный предприниматель',
                'verbose_name_plural': 'индивидуальные предприниматели',
            },
        ),
    ]