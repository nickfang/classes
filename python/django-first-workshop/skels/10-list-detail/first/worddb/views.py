from django.shortcuts import render, get_object_or_404

from worddb.models import Word


# Create your views here.
def words(request):
    pass # TODO: show all words


def detail(request, word):
    # TODO: get word
    return render("worddb/detail.html", {"word": word})
