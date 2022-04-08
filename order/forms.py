from dataclasses import fields
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'book', 'end_at', 'plated_end_at')
        labels = {
            'user': 'Читач',
            'book': 'Книга',
            #'created_at': 'Дата створенн',
            'end_at': 'End at',
            'plated_end_at': 'Plated end at',
        }
        
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: obj.surname_initials()
        self.fields['book'].label_from_instance = lambda obj: f"{obj.name}. {obj.all_authors_string()}" 
    #     self.fields['count'].required = False
        