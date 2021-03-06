# Generated by Django 2.0 on 2017-12-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canonical_name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('slug', models.SlugField()),
                ('species', models.CharField(max_length=30)),
                ('genus', models.CharField(max_length=30)),
                ('subfamily', models.CharField(blank=True, max_length=30)),
                ('family', models.CharField(max_length=30)),
                ('order', models.CharField(max_length=30)),
                ('class_name', models.CharField(db_column='class', max_length=30, verbose_name='Class')),
                ('phylum', models.CharField(max_length=30)),
                ('ncbi_id', models.PositiveSmallIntegerField(unique=True, verbose_name='NCBI ID')),
            ],
            options={
                'verbose_name': 'Species',
                'verbose_name_plural': 'Species',
                'ordering': ('species',),
            },
        ),
    ]
