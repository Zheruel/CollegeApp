# Generated by Django 3.1.2 on 2020-10-16 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0002_administrator_college_major_student_studentapplication_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentapplication',
            name='major',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='collegeapp.major'),
        ),
        migrations.AddField(
            model_name='studentapplication',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='collegeapp.student'),
        ),
    ]
