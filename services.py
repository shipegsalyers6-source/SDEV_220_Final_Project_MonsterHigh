from .models import Character


class CharacterDatabase:
    """
    Handles retrieving and organizing Monster High characters.
    """

    def get_all_characters(self):
        return Character.objects.all()

    def get_character_by_id(self, character_id):
        return Character.objects.get(id=character_id)

    def get_characters_by_wave(self, wave):
        return Character.objects.filter(wave=wave)

    def search_characters(self, search_term):
        return Character.objects.filter(
            name__icontains=search_term
        )

    def get_wave_dictionary(self):
        return {
            1: "Wave 1",
            2: "Wave 2",
            3: "Wave 3",
            4: "Wave 4",
        }


class CharacterService:
    """
    Provides application-level character functionality.
    """

    def __init__(self):
        self.database = CharacterDatabase()

    def get_characters(self, search_term="", wave=""):
        if search_term:
            characters = self.database.search_characters(search_term)

        elif wave:
            characters = self.database.get_characters_by_wave(wave)

        else:
            characters = self.database.get_all_characters()

        return characters

    def get_character(self, character_id):
        return self.database.get_character_by_id(character_id)

    def get_wave_dictionary(self):
        return self.database.get_wave_dictionary()