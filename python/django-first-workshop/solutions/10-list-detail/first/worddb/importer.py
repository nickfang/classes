import django
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "first.settings"
django.setup()

from worddb.models import Word, Pronunciation

with open("hindic.txt") as data:
    for line in data:
        word, rest = line.split(":")
        cmu, hindic = rest.split("=>")

        word = Word.objects.create(text=word.strip())
        Pronunciation.objects.create(
            word=word, system="cmu", text=cmu.strip()
        )
        Pronunciation.objects.create(
            word=word, system="hindic", text=hindic.strip()
        )
