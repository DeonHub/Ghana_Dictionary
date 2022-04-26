from django.contrib import admin
from .models import *


# Register your models here.
@admin.register( Word_In_English, Word_In_Twi, Add_English_Word, Add_Twi_Word, )

class AppAdmin(admin.ModelAdmin):
    pass
