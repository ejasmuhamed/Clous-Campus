# Generated by Django 2.2.3 on 2019-07-04 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skolr.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skolr.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('typ', models.CharField(max_length=50)),
                ('exam1', models.BooleanField()),
                ('exam2', models.BooleanField()),
                ('attendence', models.BooleanField()),
                ('assignment', models.BooleanField()),
                ('seminar', models.BooleanField(default=False)),
                ('exam1_internal_max', models.IntegerField()),
                ('exam2_internal_max', models.IntegerField()),
                ('attendence_internal_max', models.IntegerField()),
                ('assignment_internal_max', models.IntegerField()),
                ('seminar_internal_max', models.IntegerField()),
                ('semster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skolr.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.IntegerField()),
                ('register_number', models.IntegerField()),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skolr.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='InternalMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam1_internal', models.IntegerField()),
                ('exam2_internal', models.IntegerField()),
                ('attendence_internal', models.IntegerField()),
                ('assignment_internal', models.IntegerField()),
                ('seminar_internal', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skolr.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skolr.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skolr.Department'),
        ),
    ]