from django.db import models
import uuid


STATUS_CHOICES = (
    ('Inactive', 'Inactive'),
    ('Active', 'Active')
)
POSITION_CHOICES = (
    ('Manager', 'Manager'),
    ('Developer', 'Developer'),
    ('Designer', 'Designer'),
    ('Intern', 'Intern'),
)

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone_number = models.CharField(unique=True, max_length=10)
    national_id = models.CharField(unique=True, max_length=16)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(auto_now=False)
    status = models.CharField(choices=STATUS_CHOICES, default="Inactive", max_length=120)
    position = models.CharField(choices=POSITION_CHOICES, default="Developer", max_length=120)


    def __str__(self):
        return self.id
