# Generated by Django 3.2.7 on 2021-09-23 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('student_id', models.IntegerField()),
                ('student_class', models.IntegerField()),
                ('student_rollnumber', models.IntegerField()),
                ('student_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=255)),
                ('teacher_id', models.IntegerField()),
                ('teacher_email', models.IntegerField()),
                ('teacher_subject', models.CharField(max_length=255)),
            ],
        ),
    ]