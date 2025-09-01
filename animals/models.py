from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Custom user model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # The related_name for groups and permissions to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # New related name to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # New related name to avoid conflicts
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.email


# Model to store street animal details
class Animal(models.Model):
    ANIMAL_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Cow', 'Cow'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    animal_type = models.CharField(max_length=10, choices=ANIMAL_CHOICES, default='Dog')
    location = models.CharField(max_length=200)
    description = models.TextField()
    rescue_needed = models.BooleanField(default=False)
    medical_condition = models.TextField(blank=True, null=True)
    food_supply_needed = models.BooleanField(default=False)
    collar_belt_assigned = models.BooleanField(default=False)
    collar_belt_number = models.CharField(max_length=50, blank=True, null=True)
    date_rescued = models.DateField(blank=True, null=True)

    # Fixed the 'default=1' and ensured `null=True, blank=True`
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True  # Allow blank if no user is associated
    )
    image = models.ImageField(upload_to='animal_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.animal_type}: {self.name}"


# Model for Donation tracking
class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    # Default image path corrected to avoid issues with missing files
    image = models.ImageField(upload_to='donate_screenshot/', blank=True, null=True,
                              default="donate_screenshot/Screenshot_5.png")

    def __str__(self):
        return f"Donation by {self.donor_name} - {self.amount}"


# Model for Volunteer signups
class Volunteer(models.Model):
    # Changed to SET_NULL to allow users to be deleted without deleting the volunteer record
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True  # Allow blank if no user is associated
    )
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username if self.user else 'Volunteer without a user'


