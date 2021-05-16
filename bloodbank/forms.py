from django import forms
from django.forms import TextInput, Select, FileInput

from bloodbank.models import BloodOrderModel

class BloodCreateForm(forms.ModelForm):
    class Meta:
        model=BloodOrderModel
        fields=['bloodtype','required','message',]
        widgets = {
            'required': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'message': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             
        }
        
class BloodUpdateForm(forms.ModelForm):
    class Meta:
        model=BloodOrderModel
        fields=['bloodtype','required','message','status']
        widgets = {
            'required': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'message': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             
             
        }
