from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import Word_In_English, Word_In_Twi
from .form import Word_In_English_Form, Word_In_Twi_Form, TranslationForm


# Create your views here.

class MainView(FormView):
    template_name = "dictionary/index.html"
    words_in_english = Word_In_English.objects.all()
    form_classes = Word_In_English_Form, Word_In_Twi_Form
    success_url = '/'
    

    def get(self, request, *args, **kwargs):
            english_form = Word_In_English_Form()
            twi_form = Word_In_Twi_Form()
            english_word = None
            

            if request.method == 'GET':
                english_form = Word_In_English_Form(request.GET)

                if english_form.is_valid():
                    word_in_english = english_form.cleaned_data['word_in_english']
                    
                    if word_in_english:                        
                        english_word = Word_In_English.objects.filter(word_in_english= word_in_english.capitalize())
                        

                        if english_word:
                            # word_id = english_word.id
                            # print(english_word)

                            now = Word_In_English.objects.filter(word_in_english= english_word)

                            # return english_word


                            # return HttpResponse(english_word)
                            # new_word = Word_In_English.objects.filter(word_in_english= english_word)
                            # return english_word
                        else:
                            return HttpResponse("Word doesn't exist") 


            english_form = Word_In_English_Form()       

            return render(request, self.template_name, {'english_form': english_form, 'twi_form': twi_form, 'english_word': english_word})





class WordView(TemplateView, MainView):
        template_name = "dictionary/words.html"
        word_in_english = Word_In_English.objects.all()
        word_in_twi= Word_In_Twi.objects.all()

        

        def get(self, request):

            # english_word = Word_In_English.objects.filter(word_in_english: english_word)

            self.word_in_english.filter(word_in_english= MainView.english_word)
            return render(request, self.template_name, { 'word_in_twi': self.word_in_twi, 'word_in_english': self.word_in_english })

# class TwiWordView(TemplateView):
#         template_name = "dictionary/words.html"
#         word_in_twi= Word_In_Twi.objects.all()
        

#         def get(self, request):
#             return render(request, self.template_name, {'word_in_twi': self.word_in_twi})






