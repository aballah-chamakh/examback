# Generated by Django 3.0 on 2020-02-10 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=1000)),
                ('duration', models.DurationField()),
                ('total_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('finished', models.BooleanField(default=False)),
                ('exam', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('duration', models.DurationField()),
                ('object_id', models.PositiveIntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
