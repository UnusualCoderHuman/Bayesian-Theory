from django import forms
from fractions import Fraction
#Next write tests for input field 
#And display image instead
class BoxInputForm(forms.Form):
    # CharField to accept fractions
    user_input = forms.CharField(label="Enter your answer", required=True)

    def clean_user_input(self):
        # Get the user input
        user_input = self.cleaned_data.get('user_input')

        try:
            fraction_value = Fraction(user_input)
        except ValueError:
            # Raise a validation error if the input can't be converted into a fraction
            raise forms.ValidationError("Please enter a valid fraction, e.g., '3/4'. Or a decimal number like '0.25'")

        return float(fraction_value)  
class BoxCForm(forms.Form):
    red_balls = forms.IntegerField(label='Number of Red Balls', min_value=0)
    blue_balls = forms.IntegerField(label='Number of Blue Balls', min_value=0)