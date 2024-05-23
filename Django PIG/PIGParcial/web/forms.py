from django import forms
from django.core.exceptions import ValidationError

# class AltaAlumnoForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", required="True", widget=forms.TextInput(attrs={'class': 'campo_azul'}))
#     apellido = forms.CharField(label="Apellido", required="True")
#     dni = forms.IntegerField(label="DNI", required="True")
#     email = forms.EmailField(label="Email", required="True")
#     direccion = forms.CharField(label="Dirección", required="True")
    
#     def clean_nombre(self):
#         if not self.cleaned_data["nombre"].isalpha():
#             raise ValidationError("El nombre solo puede estar compuesto por letras")
        
#         return self.cleaned_data["nombre"]
    
#     def clean_apellido(self):
#         if not self.cleaned_data["apellido"].isalpha():
#             raise ValidationError("El apellido solo puede estar compuesto por letras")
        
#         return self.cleaned_data["apellido"]
    
#     def clean(self):
#         cleaned_data = super().clean()
#         nombre = cleaned_data.get("nombre")
#         apellido = cleaned_data.get("apellido")
        
#         if nombre == "Carlos" and apellido == "Lopez": #vamos a aprenderlo con BBDD para validar registros duplicados
#             raise ValidationError("El usuario Carlos Lopez ya existe")
        
#         if self.cleaned_data["dni"] < 1000000:
#             raise ValidationError("El dni debe tener 8 dígitos")
        
#         return self.cleaned_data

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea, required=True)

class SeguimientoForm(forms.Form):
    numero_orden = forms.IntegerField(label="Número de Orden", required=True)
    dni = forms.IntegerField(label="DNI", required=True)

class AdminLoginForm(forms.Form):
    numero_admin = forms.CharField(label="Administrador", max_length=10, required=True)
    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(), required=True)