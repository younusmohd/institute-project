from django.db import models
from multiselectfield import MultiSelectField


class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField()
    feedback=models.TextField(max_length=100)



class ContactData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()


    COURSES_CHOICES=(
        ('py','Python'),
        ('dj', 'Django'),
        ('ui', 'UI'),
        ('rest','REST API')
    )
    courses=MultiSelectField(max_length=200, choices=COURSES_CHOICES)

    SHIFT_CHOICES=(
        ('mrg','Morning'),
        ('aftn','Afternoon'),
        ('eveng', 'Evening'),
        ('night', 'Night')
    )
    shifts=MultiSelectField(max_length=200, choices=SHIFT_CHOICES)

    LOCATIONS_CHOICES=(
        ('hyd','Morning'),
        ('bang','Banglore'),
        ('che', 'Chennai'),
        ('pune', 'Pune')
    )
    locations = MultiSelectField(max_length=200, choices=LOCATIONS_CHOICES)

    genders = models.CharField(max_length=50)
    start_date= models.DateField(max_length=100)


class CoursesData(models.Model):
    course_id=models.IntegerField()
    course_name = models.CharField(max_length=50)
    course_dur = models.IntegerField()
    course_fee= models.IntegerField()
    start_date= models.DateField(max_length=50)
    start_time= models.TimeField(max_length=50)
    trainer_name= models.CharField(max_length=50)
    trainer_experiance = models.IntegerField()





