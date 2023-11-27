from django import forms


class HeyForm(forms.Form):
    name = forms.CharField()


class AgeForm(forms.Form):
    end = forms.IntegerField()
    birthyear = forms.IntegerField()


class OrderForm(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()
