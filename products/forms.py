from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
                    attrs={
                        'placeholder': 'Your description',
                        'rows': 20,
                        'cols': 100
                    })
        )
    price = forms.DecimalField(initial=2.99)
    class Meta():
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_email(self, **kwargs):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("We like only gmail accounts")
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
    description = forms.CharField(widget=forms.Textarea(
                attrs={
                    'placeholder': 'Your description',
                    'rows': 20,
                    'cols': 100
                })
    )
    price = forms.DecimalField(initial=2.99)


