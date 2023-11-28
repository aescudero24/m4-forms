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
    numbers = forms.CharField(
        label="Enter numbers separated by commas:",
        help_text="Example: 1, 2, 3, 4, 5",
    )

    def clean_numbers(self):
        data = self.cleaned_data["numbers"]
        try:
            numbers = [float(num.strip()) for num in data.split(",")]
        except ValueError:
            raise forms.ValidationError(
                "Invalid input. Please enter valid numbers separated by commas."
            )

        if len(numbers) < 3:
            raise forms.ValidationError("List must have at least 3 elements.")

        return numbers
