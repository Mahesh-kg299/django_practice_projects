# Generated by Django 4.1 on 2014-04-21 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_rename_enployee_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_dprt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='e_dprt', to='Api.department'),
        ),
    ]
