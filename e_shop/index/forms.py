from django import forms


class SearchFrom(forms.Form):
    search_product = forms.CharField(max_length=256)
