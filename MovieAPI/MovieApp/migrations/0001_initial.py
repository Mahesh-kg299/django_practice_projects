# Generated by Django 4.1 on 2023-05-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('g_id', models.AutoField(primary_key=True, serialize=False)),
                ('M_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('m_id', models.AutoField(primary_key=True, serialize=False)),
                ('m_title', models.CharField(max_length=50)),
                ('m_box_office', models.BigIntegerField()),
            ],
        ),
    ]
