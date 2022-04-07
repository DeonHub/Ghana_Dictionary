from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import Word_In_English, Word_In_Twi
from .form import Word_In_English_Form, Word_In_Twi_Form, TranslationForm


# Create your views here.



class WordView(TemplateView):
        template_name = "dictionary/words.html"
        word_in_english = Word_In_English.objects.all()
        word_in_twi= Word_In_Twi.objects.all()
        

        def get(self, request):
            return render(request, self.template_name, { 'word_in_twi': self.word_in_twi, 'word_in_english': self.word_in_english})

# class TwiWordView(TemplateView):
#         template_name = "dictionary/words.html"
#         word_in_twi= Word_In_Twi.objects.all()
        

#         def get(self, request):
#             return render(request, self.template_name, {'word_in_twi': self.word_in_twi})




class MainView(FormView):
    template_name = "dictionary/index.html"
    word_in_english = Word_In_English.objects.all()
    form_classes = Word_In_English_Form, Word_In_Twi_Form, TranslationForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
            english_form = Word_In_English_Form()
            twi_form = Word_In_Twi_Form()
            translations_form = TranslationForm()
            return render(request, self.template_name, {'english_form': english_form, 'twi_form': twi_form, 'translations_form': translations_form})





