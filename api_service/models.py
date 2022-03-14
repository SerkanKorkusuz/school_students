from django.core.exceptions import ValidationError
from django.db import models
from django_countries.fields import CountryField
from school_students.settings import (
    DEFAULT_SCHOOL_IMG,
    DEFAULT_STUDENT_IMG,
    UPLOAD_PATH, LOCATION_CHOICES,
    DEFAULT_LOCATION
)
from .utils import uuid_with_20


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class School(TimeStampMixin):
    name = models.CharField(max_length=20, verbose_name='School Name', unique=True)
    max_student_capacity = models.PositiveIntegerField(verbose_name='Maximum Student Capacity')
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES,
                                default=DEFAULT_LOCATION, verbose_name='Location')
    image = models.ImageField(upload_to=UPLOAD_PATH, default=DEFAULT_SCHOOL_IMG, verbose_name='School Image')

    def __str__(self):
        return self.name

    # Always save the school name with a titled word.
    def clean(self):
        self.name = self.name.title()


class Student(TimeStampMixin):
    id = models.CharField(primary_key=True, default=uuid_with_20, editable=False, max_length=20)
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    nationality = CountryField(blank_label='(Select country)', verbose_name='Nationality')
    birth_date = models.DateField(verbose_name='Birth Date')
    image = models.ImageField(upload_to=UPLOAD_PATH, default=DEFAULT_STUDENT_IMG, verbose_name='Student Image')
    school = models.ForeignKey('School', related_name='students',
                               on_delete=models.CASCADE, verbose_name='Enrolled School')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.id})'

    def save(self, *args, **kwargs):
        # Check and raise an exception if the maximum school capacity is already reached.
        if not self.school.max_student_capacity > len(self.school.students.all()):
            raise ValidationError(f'The maximum capacity of {self.school} is already reached. '
                                  f'No more students can be enrolled.')
        return super(Student, self).save(*args, **kwargs)

    # Always save the student's first name with a titled word and the last name with an uppercase word.
    def clean(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.upper()
