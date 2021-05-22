from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager
from phone_field import PhoneField

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    address=models.TextField(blank=True,null=True,default="")
    phone_number = PhoneField(blank=True, )

    pincode=models.CharField( max_length=6, default="")
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
