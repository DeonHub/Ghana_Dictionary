from django.db import models

# Create your models here.

class Word_In_English(models.Model):
    word_in_english = models.CharField(max_length=255)
    word_in_twi = models.CharField(max_length=255)
    word_meaning = models.CharField(max_length=255)
    word_in_sentence = models.CharField(max_length=255)


class Word_In_Twi(models.Model):
    word_in_twi = models.CharField(max_length=255)
    word_in_english = models.CharField(max_length=255)
    word_meaning = models.CharField(max_length=255)
    word_in_sentence = models.CharField(max_length=255)