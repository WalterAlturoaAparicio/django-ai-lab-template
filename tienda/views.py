from django.shortcuts import get_object_or_404, render, redirect
from tienda.models import Pokemon, Pedido, Entrenador
from .forms import PokemonForm, TrainerForm


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
        Pedido.objects.select_related("cliente").prefetch_related("pokemons"),
        pk=pk
    )
    return render(request, "tienda/order/order_detail.html", {"pedido": order})


def list_order(request):
    orders = Pedido.objects.select_related(
        "cliente").prefetch_related("pokemons").order_by("fecha")
    return render(request, "tienda/order/list_order.html", {"pedidos": orders})

def trainer_detail(request, pk):
    trainer = get_object_or_404(Entrenador.objects.prefetch_related("pedidos"), pk=pk)
    orders = trainer.pedidos.select_related("cliente").prefetch_related("pokemons").order_by("fecha")
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