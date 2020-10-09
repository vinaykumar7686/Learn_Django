from django import forms

class create_product_form(forms.Form):
    name = forms.CharField()
    content = forms.CharField()
    price = forms.IntegerField()