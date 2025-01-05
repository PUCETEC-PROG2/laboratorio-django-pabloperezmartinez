from django.urls import path

from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer_details, name="trainer_details"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login")
]