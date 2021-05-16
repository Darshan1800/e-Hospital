from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView,UpdateView
from supplier.decorators import user_is_supplier
from supplier.forms import OxygenCreateForms,OxygenUpdateForm
from supplier.models import OxygenOrderModel
from accounts.models import User
# Create your views here.


class DashboardView(ListView):
    
    template_name = 'supplier/supplierbase.html'
  

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_supplier)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    
    def get_queryset(self):

        return None

def createoxyrequest(request):
    if(request.method=="POST"):
        form=OxygenCreateForms(request.POST)
        if form.is_valid():
                # save article to db
                
                instance = form.save(commit=False)
                instance.oxygensupplier = request.user
                instance.save()
                return redirect("supplier:oxgyen-list")
    else:
        form=OxygenCreateForms()
        
    return render(request, 'supplier/oxygen_crete.html',{'form':form})

@login_required
def OxygenListView(request):
    oxygen=OxygenOrderModel.objects.filter(oxygensupplier=request.user).order_by('-status')
    return render(request,"supplier/oxygen_list.html",{"oxygens":oxygen})



class OxygenUpdateView(UpdateView):
    model = OxygenOrderModel
    form_class = OxygenUpdateForm
    context_object_name = 'o'
    template_name = 'supplier/oxygenedit.html'
    
    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(user_is_supplier)
    def dispatch(self, *args, **kwargs):
        self.id = kwargs['pk']
        return super(OxygenUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        item = OxygenOrderModel.objects.get(id=self.id)
        return redirect("supplier:oxgyen-list")
