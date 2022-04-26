from django import forms
from dictionary.models import Add_English_Word

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



# class Add_English_Form(forms.ModelForm):

#     model = Add_English_Word
#     fields = {"word_in_english", "word_in_twi", "word_meaning"}

#     widgets = {

#         'word_in_english': forms.TextInput(attrs={'placeholder': 'Enter a word in english'}),
#         'word_in_twi': forms.TextInput(attrs={'placeholder': 'Enter a word in twi'}),
#         'word_meaning': forms.TextInput(attrs={'placeholder': 'Enter the word meaning'})
#     }

    # word_in_english = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a word in english'}))
    # word_in_twi = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a word in twi'}))    
    # word_meaning = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a description of the word'}))    


# class Add_Twi_Form(forms.Form):
#     word_in_twi = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a word in twi'})) 
#     word_in_english = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a word in english'}))
#     word_meaning = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a description of the word'}))
