from django.contrib import admin

from .models import AttackOrSpell, Job, Player, Race, Stuff

admin.site.register(AttackOrSpell)
admin.site.register(Job)
admin.site.register(Player)
admin.site.register(Race)
admin.site.register(Stuff)
