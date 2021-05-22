from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView,UpdateView
from hospital.decorators import user_is_hospital
from hospital.forms import *
from accounts.models import User
from hospital.models import DoctorModel,RoomModel,OxygenOrderModel,PaitentModel,Ambulance
# Create your views here.
import json

from django.views.generic import FormView, TemplateView

from django.contrib.messages.views import SuccessMessageMixin


from django.core.mail import EmailMessage

class DashboardView(ListView):

    template_name = 'hospital/hospitalbase.html'


    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_hospital)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)


    def get_queryset(self):

        return None

@login_required
def createdoctor(request):
    if(request.method=="POST"):
        form=DoctorCreateForm(request.POST)
        if form.is_valid():
                # save article to db

                instance = form.save(commit=False)
                instance.hospital = request.user
                instance.save()
                return redirect("hospital:doctor-list")
    else:
        form=DoctorCreateForm()

    return render(request, 'hospital/doctorcreate.html',{'form':form})


@login_required
def createoxyrequest(request):
    mail= list(User.objects.filter(role='supplier').values_list ('email',flat=True))
    print(mail)
    if(request.method=="POST"):
        form=OxygenCreateForm(request.POST)
        if form.is_valid():
                body=form.cleaned_data['message']
                req=form.cleaned_data['required']
                email = EmailMessage('e-Hos-pital',body +"Required Oxygen Cylinder:"+str(req)+"Units" , to=mail)
                email.send()
                instance = form.save(commit=False)
                instance.oxygenhospital = request.user
                instance.save()
                return redirect("hospital:oxygen-list")
    else:
        form=OxygenCreateForm()

    return render(request, 'hospital/oxygencreate.html',{'form':form})


@login_required
def createbloodrequest(request):
    mail= list(User.objects.filter(role='bloodbank').values_list ('email',flat=True))
    print(mail)
    if(request.method=="POST"):
        form=BloodCreateForm(request.POST)
        if form.is_valid():
                # save article to db
                body=form.cleaned_data['message']
                req=form.cleaned_data['required']
                email = EmailMessage('e-Hos-pital',body +"Required Blood :"+str(req)+"Units" , to=mail)
                email.send()
                instance = form.save(commit=False)
                instance.bloodhospital = request.user
                instance.save()
                return redirect("hospital:blood-list")
    else:
        form=BloodCreateForm()

    return render(request, 'hospital/bloodcreate.html',{'form':form})




@login_required
def createrooms(request):
    if(request.method=="POST"):
        form=RoomCreateForm(request.POST)
        if form.is_valid():
                # save article to db

                instance = form.save(commit=False)
                instance.roomhospital = request.user
                instance.save()
                return redirect("hospital:room-list")
    else:
        form=RoomCreateForm()

    return render(request, 'hospital/roomcreate.html',{'form':form})


@login_required
def createpaitentrequest(request):
    if(request.method=="POST"):
        form=PaitentCreateForm(request.POST)
        if form.is_valid():
                # save article to db

                instance = form.save(commit=False)
                instance.paitenthospital = request.user
                instance.save()
                return redirect("hospital:blood-list")
    else:
        form=PaitentCreateForm()

    return render(request, 'hospital/paitentcreate.html',{'form':form})


@login_required()
def createambulancerequest(request):
    if request.method=="POST":
        form=AmbulanceCreateForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.ambhospital=request.user
            instance.save()
            return redirect("hospital:ambulance-list")
    else:
        form=AmbulanceCreateForm()
    return render(request,'hospital/ambulancecreate.html',{'form':form})



"""
Edit item
"""
class ItemUpdateView(UpdateView):
    model = DoctorModel
    form_class = DoctorStatusUpdateForm
    context_object_name = 'd'
    template_name = 'hospital/doctoredit.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_hospital)
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(ItemUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = DoctorModel.objects.get(id=self.id)
        return redirect("hospital:doctor-list")

class RoomUpdateView(UpdateView):
    model = RoomModel
    form_class = RoomUpdateForm
    context_object_name = 'r'
    template_name = 'hospital/roomedit.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_hospital)
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(RoomUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = RoomModel.objects.get(id=self.id)
        return redirect("hospital:room-list")



class OxygenUpdateView(UpdateView):
    model = OxygenOrderModel
    form_class = OxygenUpdateForm
    context_object_name = 'o'
    template_name = 'hospital/oxygenedit.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_hospital)
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(OxygenUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = OxygenOrderModel.objects.get(id=self.id)
        return redirect("hospital:oxygen-list")



class BloodUpdateView(UpdateView):
    model = BloodOrderModel
    form_class = BloodUpdateForm
    context_object_name = 'b'
    template_name = 'hospital/bloodedit.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_hospital)
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(BloodUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = OxygenOrderModel.objects.get(id=self.id)
        return redirect("hospital:blood-list")


class PaitentUpdateView(UpdateView):
    model = PaitentModel
    form_class = PaitentUpdateForm
    context_object_name = 'p'
    template_name = 'hospital/paitentedit.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_hospital)
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(PaitentUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = PaitentModel.objects.get(id=self.id)
        return redirect("hospital:paitent-list")



class AmbulanceEditView(UpdateView):
    model = Ambulance
    form_class = AmbulanceCreateForm
    context_object_name = 'a'
    template_name = 'hospital/ambulanceedit.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_hospital)
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(AmbulanceEditView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = Ambulance.objects.get(id=self.id)
        return redirect("hospital:ambulance-list")

@login_required
def DoctorListView(request):
    doctor=DoctorModel.objects.filter(hospital=request.user)
    return render(request,"hospital/doctorlist.html",{"doctors":doctor})



@login_required
def RoomListView(request):
    room=RoomModel.objects.filter(roomhospital=request.user)
    return render(request,"hospital/roomlist.html",{"rooms":room})




@login_required
def OxygenListView(request):
    oxygen=OxygenOrderModel.objects.filter(oxygenhospital=request.user).order_by('-status')
    return render(request,"hospital/oxygenlist.html",{"oxygens":oxygen})




@login_required
def BloodListView(request):
    bloods=BloodOrderModel.objects.filter(bloodhospital=request.user).order_by('-status')
    return render(request,"hospital/bloodlist.html",{"bloods":bloods})



@login_required
def PaitentListView(request):
    paitents=PaitentModel.objects.filter(paitenthospital=request.user).order_by('-oxygenstatus')
    return render(request,"hospital/paitentlist.html",{"paitents":paitents})


@login_required
def AmbulanceListView(request):
    ambulance=Ambulance.objects.filter(ambhospital=request.user).order_by('-status')
    return render(request,"hospital/ambulancelist.html",{"ambulance":ambulance})




