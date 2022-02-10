from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Bookslibrarry)
class Bookslibrarry(admin.ModelAdmin):
    list_display =['id','book_title','book_author','book_description','book_issue_date']