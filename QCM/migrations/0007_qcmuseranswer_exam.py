# Generated by Django 3.0 on 2020-02-11 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0002_auto_20200210_2033'),
        ('QCM', '0006_auto_20200211_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='qcmuseranswer',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam'),
        ),
    ]
