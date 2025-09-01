from django import forms
from .models import Animal, Donation, Volunteer, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Custom User Signup Form
class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'phone_number', 'password1', 'password2']


# Custom Login Form
class CustomLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# Form to report a street animal in need
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'animal_type', 'location', 'description', 'rescue_needed', 'medical_condition',
                  'food_supply_needed', 'collar_belt_assigned', 'collar_belt_number', 'date_rescued', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'animal_type': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'rescue_needed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'medical_condition': forms.Textarea(attrs={'class': 'form-control'}),
            'food_supply_needed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'collar_belt_assigned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'collar_belt_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_rescued': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# Donation Form with default value for 'amount'
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor_name', 'email', 'amount', 'message', 'image']
        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        self.fields['amount'].initial = 1  # Set default amount to 1


# Volunteer Form
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['contact_number', 'address']
