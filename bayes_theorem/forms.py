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
    red_balls = forms.IntegerField(label='Number of Red Balls', min_value=0, required=False)
    blue_balls = forms.IntegerField(label='Number of Blue Balls', min_value=0, required=False)
    probability_answer = forms.CharField(label='Probability of selecting a red ball', required=False)

    def clean_probability_answer(self):
        """Custom validation for probability_answer to allow fractions or decimals."""
        probability_answer = self.cleaned_data.get('probability_answer')

        if probability_answer:  # Check if the field is not empty
            try:
                # Handle fractions like '1/2' or decimals like '0.5'
                fraction_value = Fraction(probability_answer)
                return float(fraction_value)  # Return as float
            except ValueError:
                raise forms.ValidationError("Please enter a valid fraction (e.g., '3/4') or a decimal number (e.g., '0.25').")

        return probability_answer  # Return None or empty string if no input
