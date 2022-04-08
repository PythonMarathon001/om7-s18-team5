from dataclasses import fields
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
        labels = {
            'name': 'Назва книги',
            'description': 'Опис',
            'count': 'Кількість',
            'authors': 'Автори',
        }
        
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['count'].required = False
        