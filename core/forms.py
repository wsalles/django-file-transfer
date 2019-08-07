from django import forms

from .models import Book, UploadFiles


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ('file',)
