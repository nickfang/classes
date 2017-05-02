from django.contrib import admin

from worddb.models import Word, Pronunciation

admin.site.register(Word, admin.ModelAdmin)
admin.site.register(Pronunciation, admin.ModelAdmin)
