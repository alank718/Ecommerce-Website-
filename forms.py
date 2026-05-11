from django.forms import ModelForm
from .models import order,Customer,Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model=order
        fields='__all__'

class UpdateOrder(ModelForm):
    class Meta:
        model=order
        exclude=['customer']       

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'   

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'    

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]                