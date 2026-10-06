from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    wave = models.PositiveIntegerField()

    monster_type = models.CharField(
        max_length=100,
        default="To Be Completed"
    )

    personality = models.TextField(
        default="To Be Completed"
    )

    interests = models.TextField(
        default="To Be Completed"
    )

    relationships = models.TextField(
        default="To Be Completed"
    )

    background = models.TextField(
        default="To Be Completed"
    )

    additional_information = models.TextField(
        default="To Be Completed"
    )

    class Meta:
        ordering = ["wave", "name"]

    def __str__(self):
        return self.name