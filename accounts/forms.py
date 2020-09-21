from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]

class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = '__all__'

class NewRequestForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = ['Equipment', 'PONo','Delivery_Terms', 'Budget','PPMP_Date','PPMP_Signatures',
                    'PPMP_Pages','PPMP_Days','PPMP_Attachment', 'Requested_By','Requested_Date','Types_of_Procurement', 
                    'Status', 'Document_Location', 'Comments']
