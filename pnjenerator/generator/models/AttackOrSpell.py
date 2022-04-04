from django.db import models

class AttackOrSpell(models.Model):
    class Meta:
        app_label = "generator"

    name = models.CharField(max_length=64)
