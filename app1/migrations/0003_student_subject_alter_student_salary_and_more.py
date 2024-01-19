# Generated by Django 4.2.8 on 2024-01-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student_delete_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Subject',
            field=models.CharField(default='maths', max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='Salary',
            field=models.IntegerField(default=10000, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='Teacher_Name',
            field=models.CharField(default='ram', max_length=50),
        ),
    ]
