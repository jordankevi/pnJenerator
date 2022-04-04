from django.db import models

class Stuff(models.Model):
    class Meta:
        app_label = "generator"

    name = models.CharField(max_length=64)
