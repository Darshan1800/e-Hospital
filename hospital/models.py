from django.db import models
from accounts.models import User
# Create your models here.
from phone_field import PhoneField
class DoctorModel(models.Model):
    hospital = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='hospital')
    doctor_name=models.CharField(max_length=50, null=False, blank=False)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    address=models.TextField(blank=True,null=True,default="")
    status=models.BooleanField(default=False)

    class Meta:
        unique_together = ("doctor_name",)
        ordering = ('-status',)
    
    def __str__(self):
        return self.doctor_name


class RoomModel(models.Model):
    COVID = "COVID"
    GENERAL = "GENERAL"

    # CHOICES
    STATUS_CHOICES = (
        (COVID, 'COVID'),
        (GENERAL, 'GENERAL'),
    )

    roomhospital = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='roomhospital')

    room_no = models.IntegerField(null=True,blank=True,unique=True)
    room_type= models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='COVID')
    floor=models.IntegerField(null=True,blank=True)
    code=models.IntegerField(null=True,blank=True)
    no_beds=models.IntegerField(null=True,blank=True)
    filled_beds=models.IntegerField(null=True,blank=True)
    rem_beds=models.IntegerField(null=True,blank=True)
    status=models.BooleanField(default=True)


    def __str__(self):
        return str(self.room_no)
    

class OxygenOrderModel(models.Model):
    oxygenhospital = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='oxygenhospital')
    required=models.IntegerField(null=True,blank=True)
    message=models.TextField(blank=True,null=True,default="")
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.oxygenhospital.email




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
    bloodhospital = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='bloodhospital')
    bloodtype=models.CharField(blank=True,null=True,choices=STATUS_CHOICES,max_length=10)
    required=models.IntegerField(null=True,blank=True)
    message=models.TextField(blank=True,null=True,default="")
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.bloodhospital.email


class PaitentModel(models.Model):
    PAITENT_CHOICES = (
        ('ADMISSION','ADMISSION'),
        ('ONHOLD','ONHOLD'),
        ('PURSUING','PURSUING'),
        ('RECOVERED','RECOVERED'),
    
        )
    paitenthospital = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='paitenthospital')
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE,
                               related_name='doctor')
    paitentstatus=models.CharField(blank=True,null=True,choices=PAITENT_CHOICES,max_length=20)
    name=models.CharField(null=True,blank=True,max_length=50)
    disease=models.TextField(blank=True,null=True,default="")
    oxygenstatus=models.BooleanField(default=False)
    room=models.ForeignKey(RoomModel, on_delete=models.CASCADE,
                               related_name='room')
    def __str__(self):
        return self.bloodhospital.email



class Ambulance(models.Model):
    TYPE = (
        ('ICU','ICU'),
        ('OXYGEN','OXYGEN'),
        ('GENERAL','GENERAL'),
        ('COVID','COVID'),
    
        )
    ambhospital = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='ambhospital')
    ambtype=models.CharField(blank=True,null=True,choices=TYPE,max_length=20)
    drivername=models.CharField(blank=True,null=True,max_length=50)
    address=models.TextField()
    status=models.BooleanField(default=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    def __str__(self):
        return self.drivername
    
