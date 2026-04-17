from django.shortcuts import get_object_or_404, render, redirect
from django.db import transaction
from django.db.models import Sum, F
from .models import Pokemon, Pedido, Entrenador
from .forms import PokemonForm, TrainerForm, PedidoSimpleForm, PedidoItemFormSet


def home(request):
    return render(request, "tienda/home.html", {})


def list_pokemons(request):
    pokemons = Pokemon.objects.all().order_by("nombre")
    return render(request, "tienda/pokemon/list_pokemons.html", {"pokemons": pokemons})


def pokemon_detail(request, pk):
    poke = get_object_or_404(Pokemon, pk=pk)
    return render(request, "tienda/pokemon/pokemon_detail.html", {"pokemon": poke})


def order_detail1(request, pk):
    order = get_object_or_404(
        Pedido.objects.select_related(
            "cliente").prefetch_related("items__pokemon"),
        pk=pk
    )
    items = order.items.all()
    total_unidades = sum(item.cantidad for item in items)
    total_pedido = sum(item.cantidad * item.precio_unitario for item in items)

    for item in items:
        item.subtotal = item.cantidad * item.precio_unitario

    return render(request, "tienda/order/order_detail.html", {
        "pedido": order,
        "items": items,
        "total_unidades": total_unidades,
        "total_pedido": total_pedido
    })


def list_order(request):
    orders = Pedido.objects.annotate(
        total_pokemons=Sum("items__cantidad"),
        total_precio=Sum(F("items__precio_unitario") * F("items__cantidad"))
    ).select_related("cliente").order_by("-fecha")
    return render(request, "tienda/order/list_order.html", {"pedidos": orders})


def trainer_detail(request, pk):
    trainer = get_object_or_404(
        Entrenador.objects.prefetch_related("pedidos"), pk=pk)
    orders = trainer.pedidos.select_related(
        "cliente").prefetch_related("pokemons").order_by("fecha")
    return render(
        request,
        "tienda/trainer/trainer_detail.html",
        {
            "entrenador": trainer,
            "pedidos": orders
        }
    )


def create_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:list_pokemons")
    else:
        form = PokemonForm()

    return render(request, "tienda/pokemon/create_pokemon.html", {"form": form})


def edit_pokemon(request, pk):
    poke = get_object_or_404(Pokemon, pk=pk)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=poke)
        if form.is_valid():
            form.save()
            return redirect("tienda:pokemon_detail", pk=poke.pk)
    else:
        form = PokemonForm(instance=poke)

    return render(request, "tienda/pokemon/edit_pokemon.html", {"form": form, "pokemon": poke})


def delete_pokemon(request, pk):
    poke = get_object_or_404(Pokemon, pk=pk)
    if request.method == "POST":
        poke.delete()
        return redirect("tienda:list_pokemons")

    return render(request, "tienda/pokemon/delete_pokemon.html", {"pokemon": poke})


def create_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:list_pokemons")
    else:
        form = TrainerForm()

    return render(request, "tienda/trainer/create_trainer.html", {"form": form})


def edit_trainer(request, pk):
    trainer = get_object_or_404(Entrenador, pk=pk)
    if request.method == "POST":
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect("tienda:trainer_detail", pk=trainer.pk)
    else:
        form = TrainerForm(instance=trainer)

    return render(request, "tienda/trainer/edit_trainer.html", {"form": form, "entrenador": trainer})


def delete_trainer(request, pk):
    trainer = get_object_or_404(Entrenador, pk=pk)
    if request.method == "POST":
        trainer.delete()
        return redirect("tienda:list_trainers")

    return render(request, "tienda/trainer/delete_trainer.html", {"entrenador": trainer})


def delete_order(request, pk):
    order = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect("tienda:list_order")

    return render(request, "tienda/order/delete_order.html", {"pedido": order})


@transaction.atomic
def create_order_items(request):
    if request.method == "POST":
        form = PedidoSimpleForm(request.POST)
        if form.is_valid():
            order = form.save()
            formset = PedidoItemFormSet(request.POST, instance=order)
            if formset.is_valid():
                formset.save()
                return redirect("tienda:order_detail", pk=order.pk)
        else:
            form = Pedido()
            formset = PedidoItemFormSet(instance=order)
    else:
        form = PedidoSimpleForm()
        formset = PedidoItemFormSet()
    pokemons = Pokemon.objects.all()
    pokemons_dict = {str(poke.pk): poke for poke in pokemons}

    return render(request, "tienda/order/create_order_items.html", {
        "form": form,
        "formset": formset,
        "pokemons_dict": pokemons_dict
    })

@transaction.atomic
def edit_order_items(request, pk):
    order = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoSimpleForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            formset = PedidoItemFormSet(request.POST, instance=order)
            if formset.is_valid():
                formset.save()
                return redirect("tienda:order_detail", pk=order.pk)
    else:
        form = PedidoSimpleForm(instance=order)
        formset = PedidoItemFormSet(instance=order)
    pokemons = Pokemon.objects.all()
    pokemons_dict = {str(poke.pk): poke for poke in pokemons}

    return render(request, "tienda/order/edit_order_items.html", {
        "pedido": order,
        "form": form,
        "formset": formset,
        "pokemons_dict": pokemons_dict,
    })