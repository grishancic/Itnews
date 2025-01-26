from .models import Table
from django.forms import ModelForm, TextInput, Textarea


class TableForm(ModelForm):
   class Meta:
       model =Table
       fields = ['text']
       widgets = {'text': Textarea(attrs={"class": "form_control", "placeholder": "Введите текст заявки"})}

