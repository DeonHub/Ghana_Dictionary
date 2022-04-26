from django.db import models
from django.forms import ModelForm
from django import forms


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



# Recommended words
class Add_English_Word(models.Model):
    word_in_english = models.CharField(max_length=255)
    word_in_twi = models.CharField(max_length=255)
    word_meaning = models.CharField(max_length=255, null=True)


class Add_English_Form(ModelForm):

     class Meta:
        model = Add_English_Word
        fields = ['word_in_english', 'word_in_twi', 'word_meaning']

        widgets = {
        'word_in_english': forms.TextInput(attrs={'placeholder': 'Enter a word in english'}),
        'word_in_twi': forms.TextInput(attrs={'placeholder': 'Enter a word in twi'}),
        'word_meaning': forms.Textarea(attrs={'placeholder': 'Enter the word description'})
            }



# python manage.py makemigrations
# python manage.py migrate

class Add_Twi_Word(models.Model):
    word_in_twi = models.CharField(max_length=255)
    word_in_english = models.CharField(max_length=255)
    word_meaning = models.CharField(max_length=255, null=True)


class Add_Twi_Form(ModelForm):

     class Meta:
        model = Add_Twi_Word
        fields = ['word_in_twi', 'word_in_english', 'word_meaning']

        widgets = {
        'word_in_twi': forms.TextInput(attrs={'placeholder': 'Enter a word in twi'}),
        'word_in_english': forms.TextInput(attrs={'placeholder': 'Enter a word in english'}),
        'word_meaning': forms.Textarea(attrs={'placeholder': 'Enter the word description'})
            }

