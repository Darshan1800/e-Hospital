from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class SupplierRegistrationForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super(SupplierRegistrationForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['address'].label = "Address"
        self.fields['phone_number'].label = " Phone Number"
        self.fields['pincode'].label = "PinCode"

        # self.fields['gender'].widget = forms.CheckboxInput()

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Enter Address',
            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['pincode'].widget.attrs.update(
            {
                'placeholder': 'Enter PinCode',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender','address','phone_number','pincode']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            }
        }

    

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "supplier"
        if commit:
            user.save()
        return user


class HospitalRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(HospitalRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Hospital Name"
        self.fields['last_name'].label = "Hospital Manager Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['address'].label = "Address"
        self.fields['phone_number'].label = " Phone Number"
        self.fields['pincode'].label = "PinCode"


        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Hospital Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Hospital Manager Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Enter Address',
            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['pincode'].widget.attrs.update(
            {
                'placeholder': 'Enter PinCode',
            }
        )
   

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2','address','phone_number','pincode']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            }
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "hospital"
        if commit:
            user.save()
        return user


class BloodBankRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(BloodBankRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "BloodBank Name"
        self.fields['last_name'].label = "BloodBank Manager Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['address'].label = "Address"
        self.fields['phone_number'].label = " Phone Number"
        self.fields['pincode'].label = "PinCode"


        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter BloodBank Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter BloodBank Manager Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Enter Address',
            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['pincode'].widget.attrs.update(
            {
                'placeholder': 'Enter PinCode',
            }
        )
   

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2','address','phone_number','pincode']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            }
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "bloodbank"
        if commit:
            user.save()
        return user
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


# class EmployeeProfileUpdateForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super(EmployeeProfileUpdateForm, self).__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs.update(
#             {
#                 'placeholder': 'Enter First Name',
#             }
#         )
#         self.fields['last_name'].widget.attrs.update(
#             {
#                 'placeholder': 'Enter Last Name',
#             }
#         )

#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "gender"]
