__author__ = 'dl'

from django.forms import ModelForm,Form
from inetshop.models import *

class FormProduct(ModelForm):
    class Meta:
        model = Product
