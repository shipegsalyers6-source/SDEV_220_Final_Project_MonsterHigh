from django.urls import path

from . import views


app_name = "characters"


urlpatterns = [
    path("", views.home, name="home"),
    path("characters/", views.character_list, name="character_list"),
    path(
        "characters/<int:character_id>/",
        views.character_detail,
        name="character_detail",
    ),
]