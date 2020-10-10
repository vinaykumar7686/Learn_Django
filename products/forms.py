from django import forms
from products.models import Products

'''class create_product_form(forms.Form):
    name = forms.CharField()
    content = forms.CharField()
    price = forms.IntegerField()'''

class create_product_form(forms.ModelForm):
    class Meta:
        model = Products        
        fields = [
            'name',
            'content', 
            'price',
        ]

    def clean_name(self):
        val = self.cleaned_data.get('name')
        if len(val)<2:
            raise forms.ValidationError("Too Short")
        return val

    def clean_price(self):
        val = self.cleaned_data.get('price')
        if val>1000000:
            raise forms.ValidationError("To High")
        return val