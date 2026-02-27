from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField(default=0)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.CharField(max_length=255, default="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/752.png")

    def __str__(self):
        return self.nombre


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} <{self.email}>"


class Pedido(models.Model):
    ESTADOS = [
        ("CREADO", "Creado"),
        ("PAGADO", "Pagado"),
        ("ENVIADO", "Enviado"),
        ("CERRADO", "Cerrado"),
    ]

    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=7, default="CREADO", choices=ESTADOS)
    cliente = models.ForeignKey(
        Entrenador, on_delete=models.CASCADE, related_name="pedidos")
    pokemons = models.ManyToManyField(Pokemon, related_name="pedidos")

    def __str__(self):
        return f"Pedido #{self.pk} <{self.cliente.nombre} ({self.estado})>"
