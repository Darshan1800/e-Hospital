from django.shortcuts import render,redirect

from hospital.models import DoctorModel,RoomModel,OxygenOrderModel,PaitentModel,Ambulance,BloodOrderModel
from supplier.models import OxygenOrderModel as supplier
from bloodbank.models import BloodOrderModel as bloodbank
from accounts.models import User



from hospital.forms import *
def home(request):
    data={}
    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            amb=form.cleaned_data['ambtype']
            paitenttype=form.cleaned_data['paitenttype']
            oxygen=form.cleaned_data['oxygen']
            blood=form.cleaned_data['blood']
            address=form.cleaned_data['address']

            ambulance=Ambulance.objects.filter(ambtype=amb)
            data['ambulance']=ambulance

            if paitenttype=='COVID':
                rooms=RoomModel.objects.filter(filter=paitenttype)
            else:
                rooms=RoomModel.objects.filter(filter='GENERAL')

            data['rooms']=rooms

            if oxygen=="REQUIRED":
                oxygenbank_oxygen=supplier.objects.filter(status=True)
                data['oxygenbank_oxygen']=oxygenbank_oxygen

            if blood=="REQUIRED":
                bloodbank_blood=bloodbank.objects.filter(status=True)
                data['bloodbank_blood']=bloodbank_blood
            if address is not None:
                user=User.objects.filter(address__icontains=address)
            else:
                user=None

            data['user']=user
            return render(request,'search.html',data)
    else:
        form=SearchForm()
    return render(request,'home.html',{'form':form})
    