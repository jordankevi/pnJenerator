from django.db import models

class Npc(models.Model):
    class Meta:
        app_label = "generator"

    consitution = models.IntegerField()
