# Generated by Django 4.2.2 on 2023-06-28 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citasmd', '0003_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citasmd',
            name='id_citasmd',
        ),
        migrations.AddField(
            model_name='citasmd',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='citasmd.doctor'),
        ),
        migrations.AddField(
            model_name='citasmd',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='citasmd.paciente'),
        ),
    ]
