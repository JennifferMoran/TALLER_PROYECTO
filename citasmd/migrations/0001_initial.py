# Generated by Django 4.2.2 on 2023-06-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitasMd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_citasmd', models.IntegerField(null=True)),
                ('fecha_cita', models.DateField(null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
