from django import forms
from author.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',
                  'surname',
                  'patronymic',
                  )

        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'patronymic': 'Patronymic'
        }