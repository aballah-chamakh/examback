# Generated by Django 2.2 on 2020-02-11 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QCM', '0004_auto_20200211_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qcmuseranswer',
            name='qcm_question',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='QCM.QCMQuestion'),
        ),
    ]
