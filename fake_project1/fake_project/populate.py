from faker import Faker
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fake_project.settings')
django.setup()
from college.models import Student
fake = Faker()
for _ in range(int(input('Enter N :'))) :
    Student.objects.get_or_create(
        name=fake.name(),
        email=fake.email(),
        phone=fake.phone_number(),
        address=fake.address(),
        dob=fake.date_of_birth()
    )

