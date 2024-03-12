# Generated by Django 4.2.6 on 2023-12-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('material', models.CharField(max_length=100, verbose_name='Объём')),
                ('price', models.IntegerField(default=100, verbose_name='Цена')),
                ('kolvo', models.IntegerField(default=0, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]