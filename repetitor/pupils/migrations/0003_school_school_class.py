# Generated by Django 5.0 on 2023-12-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pupils', '0002_lesson_rename_pupils_pupil'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_number', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='School_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.IntegerField(max_length=1)),
                ('class_letter', models.CharField(max_length=1)),
            ],
        ),
    ]
