from django.db import models
from accounts.models import User

# Create your models here.

class BloodOrderModel(models.Model):
    STATUS_CHOICES = (
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B+", "B-"),
    ("AB+","AB+"),
    ("AB-","AB-"),
    ("O+","O+"),
    ("O-","O-")
)
    blooduser = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blooduser')
    bloodtype=models.CharField(blank=True,null=True,choices=STATUS_CHOICES,max_length=10)
    required=models.IntegerField(null=True,blank=True)
    message=models.TextField(blank=True,null=True,default="")
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.blooduser.email
