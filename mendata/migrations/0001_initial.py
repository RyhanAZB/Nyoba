# Generated by Django 4.0.4 on 2022-04-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nim', models.CharField(max_length=100)),
                ('kelas', models.CharField(max_length=100)),
                ('jurusan', models.CharField(max_length=100)),
                ('status_asisten', models.CharField(choices=[('Praktikum', 'Praktikum'), ('Riset', 'Riset')], default='Praktikum', max_length=20)),
                ('status_data', models.CharField(choices=[('Aktif', 'Aktif'), ('Calon', 'Calon'), ('Tidak Aktif', 'Tidak Aktif'), ('Mantan', 'Mantan')], default='Aktif', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'data',
            },
        ),
    ]
