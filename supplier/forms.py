from django import forms
from django.forms import TextInput, Select, FileInput
from supplier.models import OxygenOrderModel 


class OxygenCreateForms(forms.ModelForm):
    class Meta:
        model = OxygenOrderModel
        fields = ['no_cylinder','message','status']
        widgets = {
            'no_cylinder': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'message': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             
             
        }

        
class OxygenUpdateForm(forms.ModelForm):
    class Meta:
        model=OxygenOrderModel
        fields=['no_cylinder','message','status']
        widgets = {
            'no_cylinder': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'message': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             
             
        }