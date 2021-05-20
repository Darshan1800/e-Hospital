from django import forms
from django.forms import TextInput, Select, FileInput

from hospital.models import DoctorModel,RoomModel,OxygenOrderModel,BloodOrderModel,PaitentModel,Ambulance


class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model=DoctorModel
        fields=['doctor_name','address','phone_number']
        widgets = {
            'doctor_name': TextInput(attrs={
                                     'name': "doctor-name",
                                     'class': "form-control",
                                     'placeholder': "Enter Doctor Name",
                                     'id': "doctorName"
                                     })
        }

class DoctorStatusUpdateForm(forms.ModelForm):
    class Meta:
        model=DoctorModel
        fields=['doctor_name','address','phone_number','status',]
        

        
class RoomCreateForm(forms.ModelForm):
    class Meta:
        model=RoomModel
        fields=['room_no','room_type','floor','code','no_beds','filled_beds','rem_beds','status']
        widgets = {
            'room_no': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'floor': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'code': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'no_beds': TextInput(attrs={
                                     'class': "form-control",
                                     }),
                 'filled_beds': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'rem_beds': TextInput(attrs={
                                     'class': "form-control",
                                     })
        }
        
class RoomUpdateForm(forms.ModelForm):
    class Meta:
        model=RoomModel
        fields=['room_no','room_type','floor','code','no_beds','filled_beds','rem_beds','status']
        widgets = {
            'room_no': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'floor': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'code': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'no_beds': TextInput(attrs={
                                     'class': "form-control",
                                     }),
                 'filled_beds': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'rem_beds': TextInput(attrs={
                                     'class': "form-control",
                                     })
        }



       
class OxygenCreateForm(forms.ModelForm):
    class Meta:
        model=OxygenOrderModel
        fields=['required','message',]
        widgets = {
            'required': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'message': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             
        }
        
class OxygenUpdateForm(forms.ModelForm):
    class Meta:
        model=OxygenOrderModel
        fields=['required','message','status']
        widgets = {
            'required': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             'message': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             
             
        }


  
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



       
class PaitentCreateForm(forms.ModelForm):
    class Meta:
        model=PaitentModel
        fields=['doctor','paitentstatus','name','disease','oxygenstatus','room']
     
        widgets = {
           
             'name': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             
             
        }
    
class PaitentUpdateForm(forms.ModelForm):
    class Meta:
        model=PaitentModel
        fields=['doctor','paitentstatus','name','disease','oxygenstatus','room']
     
        widgets = {
           
             'name': TextInput(attrs={
                                     'class': "form-control",
                                     }),
             
             
        }
    

class AmbulanceCreateForm(forms.ModelForm):
    class Meta:
        model=Ambulance
        fields=['drivername','ambtype','address','status','phone_number']

class SearchForm(forms.Form):
    TYPE = (
        ('ICU','ICU'),
        ('OXYGEN','OXYGEN'),
        ('GENERAL','GENERAL'),
        ('COVID','COVID'),
    
        )
    PATTYPE=(
        ('COVID','COVID'),
        ('NON-COVID','NON-COVID'),
    )
    REQUIRED=(
        ('REQUIRED','REQUIRED'),
        ('NOT-REQUIRED','NOT-REQUIRED'),
    )
    ambtype=forms.ChoiceField(choices=TYPE)
    paitenttype=forms.ChoiceField(choices=PATTYPE)
    oxygen=forms.ChoiceField(choices=REQUIRED)
    blood=forms.ChoiceField(choices=REQUIRED)
    address=forms.CharField()