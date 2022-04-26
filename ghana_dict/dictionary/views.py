from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
from .models import Add_English_Word, Add_Twi_Word, Word_In_English, Word_In_Twi, Add_English_Form, Add_Twi_Form
from .form import Word_In_English_Form, Word_In_Twi_Form
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# from gTTS.templatetags.gTTS import say
import os




# Create your views here.

class MainView(FormView):
    template_name = "dictionary/index.html"
    words_in_english = Word_In_English.objects.all()
    word_in_english = ""
    word_in_twi = ""
    form_classes = Word_In_English_Form, Word_In_Twi_Form
    text = "Text From Views"
    

    def get(self, request):
            english_form = Word_In_English_Form()
            twi_form = Word_In_Twi_Form()
            english_word = None            

            if request.method == 'GET':
                english_form = Word_In_English_Form(request.GET)
                twi_form = Word_In_Twi_Form(request.GET)

                if english_form.is_valid():
                    self.word_in_english = english_form.cleaned_data['word_in_english']
                    
                    if self.word_in_english:                        
                        english_word = Word_In_English.objects.filter(word_in_english= self.word_in_english.capitalize())
                        

                        if english_word:
                            return redirect('/english_word')
                        else:
                            return HttpResponse("Word doesn't exist") 


                if twi_form.is_valid():
                    self.word_in_twi = twi_form.cleaned_data['word_in_twi']
                    
                    if self.word_in_twi:                        
                        twi_word = Word_In_Twi.objects.filter(word_in_twi= self.word_in_twi.capitalize())
                        

                        if twi_word:
                            return redirect('/twi_word')
                        else:
                            return HttpResponse("Word doesn't exist") 


            english_form = Word_In_English_Form()       
            twi_form = Word_In_Twi_Form()       


            return render(request, self.template_name, {
                'english_form': english_form, 
                'twi_form': twi_form, 
                'words_in_english': Word_In_English.objects.all().filter(word_in_english= self.word_in_english.capitalize()),
                'words_in_twi': Word_In_Twi.objects.all().filter(word_in_twi= self.word_in_twi.capitalize()),
                'text': self.text,
                })
         



class EnglishWordView(TemplateView):
        template_name = "dictionary/english_words.html"
        words_in_english = Word_In_English.objects.all()
        word_in_english = ""
        
        def get(self, request): 
            if request.method == 'GET':
                    english_form = Word_In_English_Form(request.GET)

                    if english_form.is_valid():
                        self.word_in_english = english_form.cleaned_data['word_in_english']

                    else:
                        return HttpResponse("Search")        

            return render(request, self.template_name, { 
                'words_in_english': self.words_in_english.filter(word_in_english= self.word_in_english.capitalize()), 
                'other_words': Word_In_English.objects.all().order_by("word_in_english"),
                'close_words': self.words_in_english.filter(word_in_english__icontains= self.word_in_english), 
                })
        


class TwiWordView(TemplateView):
        template_name = "dictionary/twi_words.html"
        words_in_twi= Word_In_Twi.objects.all()
        word_in_twi = ""
        
        def get(self, request):  
            if request.method == 'GET':
                    twi_form = Word_In_Twi_Form(request.GET)

                    if twi_form.is_valid():
                        self.word_in_twi = twi_form.cleaned_data['word_in_twi']

                    else:
                        return HttpResponse("Search")        

            return render(request, self.template_name, { 
                'words_in_twi': self.words_in_twi.filter(word_in_twi= self.word_in_twi.capitalize()),
                'other_words': Word_In_Twi.objects.all().order_by("word_in_twi"),
                'close_words': self.words_in_twi.filter(word_in_twi__icontains= self.word_in_twi), 
                })
        



class AddEnglishWordView(SuccessMessageMixin, CreateView):
    model = Add_English_Word
    form_class = Add_English_Form
    template_name = "dictionary/add_english.html"
    success_url = "/"
    success_message = "Request successful"
    added_english_words = Add_English_Word.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["added_english_words"] = self.added_english_words
        return context



class AddTwiWordView(SuccessMessageMixin, CreateView):
    model = Add_Twi_Word
    form_class = Add_Twi_Form
    template_name = "dictionary/add_twi.html"
    success_url = "/"
    success_message = "Request successful"
    added_twi_words = Add_Twi_Word.objects.all()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["added_twi_words"] = self.added_twi_words
        return context    
