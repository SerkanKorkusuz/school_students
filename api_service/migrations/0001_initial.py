# Generated by Django 4.0.3 on 2022-03-13 21:32

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='School Name')),
                ('max_student_capacity', models.PositiveIntegerField(verbose_name='Maximum Student Capacity')),
                ('location', models.CharField(choices=[('bangkok', 'Thailand-Bangkok'), ('nonthaburi', 'Thailand-Nonthaburi'), ('songkhla', 'Thailand-Songkhla'), ('chonburi', 'Thailand-Chonburi'), ('surat-thani', 'Thailand-Surat Thani'), ('chiang-mai', 'Thailand-Chiang Mai'), ('pattaya', 'Thailand-Pattaya'), ('istanbul', 'Turkey-Istanbul'), ('ankara', 'Turkey-Ankara'), ('malatya', 'Turkey-Malatya')], default='bangkok', max_length=20, verbose_name='Location')),
                ('image', models.ImageField(default='static/img/default-school.jpg', upload_to='static/uploads/', verbose_name='School Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('nationality', django_countries.fields.CountryField(max_length=2, verbose_name='Nationality')),
                ('birth_date', models.DateField(verbose_name='Birth Date')),
                ('image', models.ImageField(default='static/img/default-student.jpg', upload_to='static/uploads/', verbose_name='Student Image')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='api_service.school', verbose_name='Enrolled School')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
