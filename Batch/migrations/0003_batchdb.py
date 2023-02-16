# Generated by Django 4.1.5 on 2023-02-01 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Batch', '0002_trainer_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchDB',
            fields=[
                ('bid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Time', models.TimeField()),
                ('room_no', models.CharField(choices=[['201', '201'], ['301', '301'], ['302', '302'], ['501', '501'], ['502', '502'], ['webonline', 'webonline']], max_length=10)),
                ('mode', models.CharField(choices=[['Online', 'Online'], ['Offline', 'Offline']], max_length=10)),
                ('Trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Batch.trainer')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Batch.subject')),
            ],
        ),
    ]
