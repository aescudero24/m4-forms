from django import forms


class FrontTimesForm(forms.Form):
    string = forms.CharField()
    number = forms.IntegerField()


class NoTeenSumForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()


class XyzThereForm(forms.Form):
    string = forms.CharField()


class CenteredAverageForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    c = forms.IntegerField()
    d = forms.IntegerField(required=False)
    e = forms.IntegerField(required=False)
    f = forms.IntegerField(required=False)
    g = forms.IntegerField(required=False)
