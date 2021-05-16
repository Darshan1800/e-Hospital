from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from accounts.forms import *
from accounts.models import User


class RegisterHospitalView(CreateView):
    model = User
    form_class = HospitalRegistrationForm
    template_name = 'accounts/Hospital/hospital_register.html'


    extra_context = {
        'title': 'Register'
    }

    def post(self,request,*args,**kwargs):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request,'accounts/Hospital/hospital_register.html',{'form':form})


class RegisterBloodBankView(CreateView):
    model = User
    form_class = BloodBankRegistrationForm
    template_name = 'accounts/bloodbank/bloodbank_register.html'
    success_url = '/'

    extra_context = {
        'title': 'Register'
    }

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/bloodbank/bloodbank_register.html', {'form': form})



class RegisterSupplierBankView(CreateView):
    model = User
    form_class = SupplierRegistrationForm
    template_name = 'accounts/supplier/supplier_register.html'
    success_url = '/'

    extra_context = {
        'title': 'Register'
    }

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/supplier/supplier_register.html', {'form': form})

class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    extra_context = {
        'title': 'Login'
    }

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)
