from tienda.models import Pokemon, Entrenador, Pedido
from django.db.models import Avg, Count, Max
from django.utils.timezone import now

#consultas individuales a POKEMON
Pokemon.objects.all()
Pokemon.objects.filter(precio__gt=100)
Pokemon.objects.filter(precio__lte=50)
Pokemon.objects.get(nombre="Venusaur")
Pokemon.objects.filter(nombre__icontains="char")
Pokemon.objects.order_by("precio")
Pokemon.objects.order_by("-numero")
Pokemon.objects.values("nombre", "precio")
Pokemon.objects.aggregate(promedio=Avg("precio"))
Pokemon.objects.aggregate(maximo=Max("precio"))

#Consultas individuales a ENTRENADOR
Entrenador.objects.filter(activo=True)
Entrenador.objects.filter(fecha_registro__date=now().date())
Entrenador.objects.get(email="ash.ketchum@pokeleague.com")
Entrenador.objects.count()
Entrenador.objects.order_by("-fecha_registro")[:5]

#Consultas individuales a PEDIDO
Pedido.objects.filter(estado="CREADO")
Pedido.objects.filter(estado="PAGADO")
Pedido.objects.filter(estado="ENVIADO").count()
Pedido.objects.order_by("-fecha")
Pedido.objects.values("estado").annotate(total=Count("id"))


#Consultas PEDIDO + ENTRENADOR
Pedido.objects.filter(cliente__nombre="Ash")
Pedido.objects.filter(cliente__activo=True)
Entrenador.objects.filter(pedidos__isnull=False).distinct()
Entrenador.objects.filter(fecha_registro__date=now().date())
Pedido.objects.values("id", "cliente__email", "estado")

#Consultas PEDIDO + POKEMON
Pedido.objects.filter(pokemons__nombre="Pikachu")
Pokemon.objects.filter(pedidos__isnull=False).distinct()
Pokemon.objects.annotate(total_pedidos=Count("pedidos"))
Pedido.objects.filter(pokemons__precio__gt=100).distinct()
Pokemon.objects.filter(pedidos__estado="PAGADO").distinct()


#Consulta PEDIDO + POKEMON + ENTRENADOR
Pokemon.objects.filter(pedidos__cliente__nombre="Misty").distinct()
Pedido.objects.filter(
    estado="PAGADO",
    cliente__activo=True,
    pokemons__precio__gt=100
).distinct()
Entrenador.objects.annotate(
    total_pokemons=Count("pedidos__pokemons")
)
Entrenador.objects.filter(
    pedidos__pokemons__nombre="Charizard"
).distinct()
Entrenador.objects.values(
    "nombre", "pedidos__estado"
).annotate(
    total=Count("pedidos")
)