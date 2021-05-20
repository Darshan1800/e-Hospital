from django.shortcuts import render,redirect

from hospital.models import DoctorModel,RoomModel,OxygenOrderModel,PaitentModel,Ambulance,BloodOrderModel
from supplier.models import OxygenOrderModel as supplier
from bloodbank.models import BloodOrderModel as bloodbank
from accounts.models import User
from django.db.models import Sum


from hospital.forms import *

def about(request):
    return render(request,'about.html')
def home(request):
    data={}
    data['hospital_count']=User.objects.filter(role='hospital').count()
    data['bloodbank_count']=User.objects.filter(role='bloodbank').count()
    data['supplier_count']=User.objects.filter(role='supplier').count()
    res1=bloodbank.objects.aggregate(Sum('required'))
    res2=supplier.objects.aggregate(Sum('no_cylinder'))
    data['blood_count']=res1['required__sum']
    data['oxygen_count']=res2['no_cylinder__sum']
    data['room_count']=RoomModel.objects.aggregate(Sum('no_beds'))['no_beds__sum']

    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            amb=form.cleaned_data['ambtype']
            paitenttype=form.cleaned_data['paitenttype']
            oxygen=form.cleaned_data['oxygen']
            blood=form.cleaned_data['blood']
            address=form.cleaned_data['address']

            ambulance=Ambulance.objects.filter(ambtype=amb,status=True)
            data['ambulance']=ambulance

            if paitenttype=='COVID':
                rooms=RoomModel.objects.filter(room_type=paitenttype,status=True)
            else:
                rooms=RoomModel.objects.filter(room_type='GENERAL',status=True)

            data['rooms']=rooms

            if oxygen=="REQUIRED":
                oxygenbank_oxygen=supplier.objects.filter(status=True)
                data['oxygenbank_oxygen']=oxygenbank_oxygen

            if blood=="REQUIRED":
                bloodbank_blood=bloodbank.objects.filter(status=True)
                data['bloodbank_blood']=bloodbank_blood
            if address is not None:
                user=User.objects.filter(address__icontains=address,role='hospital')
            else:
                user=None

            data['user']=user
            return render(request,'search.html',data)
    else:
        form=SearchForm()
        data['form']=form
    return render(request,'home.html',data)
    