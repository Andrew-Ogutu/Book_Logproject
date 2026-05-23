from django import forms

from .models import Book, Entry



class BookForm(forms.ModelForm):
    class Meta:
        model=Book

        fields=['title', 'author']
        labels={'title':'Title', 'author':'Author'}



