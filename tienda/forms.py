from django import forms
from django.forms import inlineformset_factory
from .models import Pokemon, Entrenador, PedidoItem, Pedido


class PokemonForm(forms.ModelForm):
    def clean_precio(self):
        # si el precio es negativo, se lanza un error de validacion
        precio = self.cleaned_data.get("precio")
        if precio is None and precio <= 0:
            raise forms.ValidationError(
                "El precio debe ser un valor positivo.")

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


class PedidoSimpleForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado']


class PedidoItemsForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = ['pokemon', 'cantidad', 'precio_unitario']
        widgets = {
            'pokemon': forms.Select(attrs={
                'class': 'form-control'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Cantidad'
            }),
            'precio_unitario': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Precio Unitario'
            }),
        }


PedidoItemFormSet = inlineformset_factory(
    Pedido,
    PedidoItem,
    form=PedidoItemsForm,
    extra=1,
    can_delete=True
)
