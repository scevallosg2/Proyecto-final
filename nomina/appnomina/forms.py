from django import forms
from .models import Cargo, Departamento, Empleado
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese cargo',
                'class':'form-group',
                'required':True
            }),            
        }
class DepartamentoFrom(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese departamento',
                'class':'form-group',
                'required':True
            }),            
        }
class EmpleadoFrom(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['id','nombre','cedula','cargo','departamento','sueldo','estado']
        widgets = {
            'id':forms.TextInput(attrs={
                'placeholder':'Ingrese id',
                'class':'form-group',
                'type' : 'number',
                'required':True
            }),
            'nombre':forms.TextInput(attrs={
                'placeholder':'Ingrese empleado',
                'class':'form-group',
                'required':True
            }), 
            
            'cedula':forms.TextInput(attrs={
                'placeholder':'Escriba su cedula',
                'class':'form-group',
                'type':"number",
                'required':True
            }),   
            
            'sueldo':forms.TextInput(attrs={
                'placeholder':'Ingrese sueldo',
                'class':'form-group',
                'type':"number",
                'required':True
            
            }),           
        }                  
          

                
