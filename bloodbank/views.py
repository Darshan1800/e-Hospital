from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from bloodbank.decorators import user_is_bloodbank

from accounts.models import User

from .models import BloodOrderModel
from .forms import *
# Create your views here.


class DashboardView(ListView):
    
    template_name = 'bloodbank/bloodbankbase.html'
  

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_bloodbank)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    
    def get_queryset(self):

        return None




@login_required
def BloodListView(request):
    bloods=BloodOrderModel.objects.filter(blooduser=request.user).order_by('-status')
    return render(request,"bloodbank/bloodlist.html",{"bloods":bloods})




def createbloodrequest(request):
    if(request.method=="POST"):
        form=BloodCreateForm(request.POST)
        if form.is_valid():
                # save article to db
                
                instance = form.save(commit=False)
                instance.blooduser = request.user
                instance.save()
                return redirect("bloodbank:blood-list")
    else:
        form=BloodCreateForm()
        
    return render(request, 'bloodbank/bloodcreate.html',{'form':form})





class BloodUpdateView(UpdateView):
    model = BloodOrderModel
    form_class = BloodUpdateForm
    context_object_name = 'b'
    template_name = 'bloodbank/bloodedit.html'
    
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_bloodbank)
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(BloodUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = BloodOrderModel.objects.get(id=self.id)
        return redirect("bloodbank:blood-list")


