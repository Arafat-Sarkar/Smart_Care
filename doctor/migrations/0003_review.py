# Generated by Django 4.2.7 on 2025-04-03 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        ('doctor', '0002_remove_doctor_available_time_doctor_available_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('⭐ ', '⭐'), ('⭐ ⭐', '⭐ ⭐'), ('⭐ ⭐ ⭐', '⭐ ⭐ ⭐'), ('⭐ ⭐ ⭐ ⭐', '⭐ ⭐ ⭐ ⭐'), ('⭐ ⭐ ⭐ ⭐ ⭐', '⭐ ⭐ ⭐ ⭐ ⭐')], max_length=30)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
