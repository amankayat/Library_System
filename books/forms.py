from django import forms
from books.models import book_data
class library_system(forms.ModelForm):
    class Meta:
        model = book_data
        fields =['name','author','year']
        widgets ={'name':forms.TextInput(attrs={'class':'form-control'}),
        'author':forms.TextInput(attrs={'class':'form-control'}),
        'year':forms.TextInput(attrs={'class':'form-control',})}
        labels ={'year':'Publication_Year'}