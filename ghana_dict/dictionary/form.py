from django import forms

translations =(
    ("1", "English to Twi"),
    ("2", "Twi to English"),
)


class TranslationForm(forms.Form):
    translations = forms.ChoiceField(choices = translations)


class Word_In_English_Form(forms.Form):
    word_in_english = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter an English word to search'}), max_length=150)

class Word_In_Twi_Form(forms.Form):
    word_in_twi = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter an Twi word to search'}), max_length=150)