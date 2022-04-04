from django.db import models

from .AttackOrSpell import AttackOrSpell
from .Job import Job
from .Race import Race
from .Stuff import Stuff

class Player(models.Model):
    class Meta:
        app_label = "generator"

    name = models.CharField(max_length=32)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    level = models.IntegerField()
    alignment = models.CharField(max_length=30)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    wisdom = models.IntegerField()
    intelligence = models.IntegerField()
    charisma = models.IntegerField()
    proficiencies = models.JSONField()
    other_prof_languages = models.TextField(null=True)
    inspiration = models.BooleanField(null=True)
    stuff = models.ForeignKey(Stuff, on_delete=models.SET_NULL, null=True)
    personality = models.TextField(null=True)
    ideals = models.TextField(null=True)
    bonds = models.TextField(null=True)
    flaws = models.TextField(null=True)
    features = models.TextField(null=True)
    maxHp = models.IntegerField()
    currentHp = models.IntegerField()
    attacks_and_spells = models.ManyToManyField(AttackOrSpell)
    inventory = models.JSONField(null=True)
    notes = models.TextField(null=True)
