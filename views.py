from django.shortcuts import get_object_or_404, render

from .models import Character
from .services import CharacterService


def home(request):
    service = CharacterService()

    characters = service.get_characters()
    waves = service.get_wave_dictionary()

    context = {
        "characters": characters,
        "waves": waves,
        "character_count": characters.count(),
    }

    return render(
        request,
        "characters/home.html",
        context
    )


def character_list(request):
    service = CharacterService()

    search_term = request.GET.get("search", "").strip()
    wave = request.GET.get("wave", "").strip()

    characters = service.get_characters(
        search_term=search_term,
        wave=wave
    )

    waves = service.get_wave_dictionary()

    context = {
        "characters": characters,
        "waves": waves,
        "search_term": search_term,
        "selected_wave": wave,
    }

    return render(
        request,
        "characters/character_list.html",
        context
    )


def character_detail(request, character_id):
    character = get_object_or_404(
        Character,
        id=character_id
    )

    return render(
        request,
        "characters/character_detail.html",
        {
            "character": character
        }
    )
