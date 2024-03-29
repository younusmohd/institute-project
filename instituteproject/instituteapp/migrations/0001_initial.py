# Generated by Django 2.2.3 on 2019-07-30 06:50

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('courses', multiselectfield.db.fields.MultiSelectField(choices=[('py', 'Python'), ('dj', 'Django'), ('ui', 'UI'), ('rest', 'REST API')], max_length=200)),
                ('shifts', multiselectfield.db.fields.MultiSelectField(choices=[('mrg', 'Morning'), ('aftn', 'Afternoon'), ('eveng', 'Evening'), ('night', 'Night')], max_length=200)),
                ('locations', multiselectfield.db.fields.MultiSelectField(choices=[('hyd', 'Morning'), ('bang', 'Banglore'), ('che', 'Chennai'), ('pune', 'Pune')], max_length=200)),
                ('genders', models.CharField(max_length=50)),
                ('start_date', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('course_name', models.CharField(max_length=50)),
                ('course_dur', models.IntegerField()),
                ('course_fee', models.IntegerField()),
                ('start_date', models.DateField(max_length=50)),
                ('start_time', models.TimeField(max_length=50)),
                ('trainer_name', models.CharField(max_length=50)),
                ('trainer_experiance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('feedback', models.TextField(max_length=100)),
            ],
        ),
    ]
