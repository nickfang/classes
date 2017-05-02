from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    __unicode__ = __str__


class Pronunciation(models.Model):
    word = models.ForeignKey(Word)
    system = models.CharField(
        max_length=20, choices=[("cmu", "CMU"), ("hindic", "Hindic")]
    )
    text = models.CharField(max_length=100)

    def __str__(self):
        return "{}[{}]: {}".format(self.word, self.system, self.text)

    __unicode__ = __str__
