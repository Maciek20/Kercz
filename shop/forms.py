from datetime import datetime
from itertools import product
from django.contrib.auth.models import User
from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.utils.translation import gettext_lazy as _

from .models import *

class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=("client_id","product_id","quantity","size")