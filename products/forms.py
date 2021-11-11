from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs=
                                                                  {"placeholder": "My title", "type": "text"}))
    description = forms.CharField()  # or leave for the default
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]
class RawProductForm(forms.Form):
    title = forms.CharField(label= "Title",widget=forms.TextInput(attrs=
                                                   {"placeholder":"My title", "type":"text"}))#the same way we change in html
    description = forms.CharField() #or leave for the default
    price = forms.DecimalField()
