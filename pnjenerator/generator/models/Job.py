from django.db import models

class Job(models.Model):
    class Meta:
        app_label = "generator"

    name = models.CharField(max_length=16)
