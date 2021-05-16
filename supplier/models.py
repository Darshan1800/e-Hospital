from django.db import models
from accounts.models import User


# Create your models here.

class OxygenOrderModel(models.Model):
    oxygensupplier = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='oxygensupplier')
    no_cylinder=models.IntegerField(null=True,blank=True)
    message=models.TextField(blank=True,null=True,default="")
    status=models.BooleanField(default=False)

    def _str_(self):
        return self.oxygensupplier.email