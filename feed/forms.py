from django import forms
from .models import Feed

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ('description', 'document', )