from django.shortcuts import render, get_object_or_404

from worddb.models import Word


# Create your views here.
def words(request):
    return render(request, "worddb/words.html", {"words": Word.objects.all()})


def detail(request, word):
    word = get_object_or_404(Word, text__iexact=word)
    return render(request, "worddb/detail.html", {"word": word})
