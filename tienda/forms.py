from django import forms
from .models import Pokemon, Entrenador


class PokemonForm(forms.ModelForm):
    def clean_precio(self):
        #si el precio es negativo, se lanza un error de validacion
        precio = self.cleaned_data.get("precio")
        if precio is None and precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        
        return precio
    


    class Meta:
        model = Pokemon
        fields = ['nombre', 'descripcion', 'imagen', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del Pokemon'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Descripción del Pokemon'
            }),
            'imagen': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'URL de la imagen'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control', 
                'step': '0.01',
                'min': '0',
                'placeholder': 'Precio del Pokemon'
            }),
        }
    
class TrainerForm(forms.ModelForm): 
    class Meta: 
        model = Entrenador 
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del Entrenador'
            }), 
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email del Entrenador'
            }),
        }

