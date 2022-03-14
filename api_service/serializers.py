from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from django_countries.serializer_fields import CountryField
from school_students.settings import DEFAULT_LOCATION, LOCATION_CHOICES
from .models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)
    max_student_capacity = serializers.IntegerField(min_value=1)
    location = serializers.ChoiceField(choices=LOCATION_CHOICES, required=False, default=DEFAULT_LOCATION)

    class Meta:
        model = School
        exclude = ['created_at', 'updated_at', 'image']


class StudentSerializer(CountryFieldMixin, serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    nationality = CountryField(required=False, default='TH')
    birth_date = serializers.DateField()
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = Student
        exclude = ['created_at', 'updated_at', 'image']
