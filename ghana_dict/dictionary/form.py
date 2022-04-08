from django import forms

translations =(
    ("1", "English to Twi"),
    ("2", "Twi to English"),
)


class TranslationForm(forms.Form):
    translations = forms.ChoiceField(choices = translations)



class Word_In_English_Form(forms.Form):
    word_in_english = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a word in english'}))

class Word_In_Twi_Form(forms.Form):
    word_in_twi = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a word in twi'}))