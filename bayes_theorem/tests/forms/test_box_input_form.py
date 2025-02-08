from django.test import TestCase
from bayes_theorem.forms import BoxInputForm
# from views  import balls_in_box
from bayes_theorem.config import correct_answers_for_box

class BoxInputFormTestCase(TestCase):
    def setUp(self):
        self.valid_fraction = {'user_input': 4/5}
        self.valid_decimal = {'user_input': 0.67}
        self.invalid_not_number = {'user_input': 'Lorem Ipsum'}
        self.invalid_blank = {'user_input': ''}
        self.correct_answer_box_a_decimal = {'user_input': 0.5}
        self.correct_answer_box_a_fraction = {'user_input': 1/2}
        self.correct_answer_box_a_fraction_variant = {'user_input': 50/100}
        self.incorrect_answer_box_a_or_b_decimal = {'user_input': 0.9}
        self.incorrect_answer_box_a_or_b_fraction = {'user_input': 2/3}
        self.correct_answer_box_b_decimal = {'user_input': 0.75}
        self.correct_answer_box_b_fraction = {'user_input': 3/4}
        self.correct_answer_box_b_fraction_variant = {'user_input': 150/200}
    

    def test_form_rejects_invalid_blank(self):
        form = BoxInputForm(data=self.invalid_blank)
        self.assertFalse(form.is_valid())
    
    def test_form_rejects_invalid_input_not_number(self):
        form = BoxInputForm(data=self.invalid_not_number)
        self.assertFalse(form.is_valid())

    def test_form_accepts_valid_input_fraction(self):
        form = BoxInputForm(data=self.valid_fraction)
        self.assertTrue(form.is_valid())

    def test_form_accepts_valid_input_decimal(self):
        form = BoxInputForm(data=self.valid_decimal)
        self.assertTrue(form.is_valid())

    def test_box_a_correct_answer_decimal(self):
        form = BoxInputForm(data=self.correct_answer_box_a_decimal)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertEqual(form.cleaned_data['user_input'], correct_answers_for_box['A'])
    
    def test_box_a_correct_answer_fraction(self):
        form = BoxInputForm(data=self.correct_answer_box_a_fraction)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertEqual(form.cleaned_data['user_input'], correct_answers_for_box['A'])

    def test_box_a_correct_answer_fraction_variant(self):
        form = BoxInputForm(data=self.correct_answer_box_a_fraction_variant)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertEqual(form.cleaned_data['user_input'], correct_answers_for_box['A'])
    
    def test_box_a_incorrect_answer_decimal(self):
        form = BoxInputForm(data=self.incorrect_answer_box_a_or_b_decimal)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertNotEqual(form.cleaned_data['user_input'], correct_answers_for_box['A'])
    
    def test_box_a_incorrect_answer_fraction(self):
        form = BoxInputForm(data=self.incorrect_answer_box_a_or_b_fraction)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertNotEqual(form.cleaned_data['user_input'], correct_answers_for_box['A'])
    

    def test_box_b_correct_answer_decimal(self):
        form = BoxInputForm(data=self.correct_answer_box_b_decimal)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertEqual(form.cleaned_data['user_input'], correct_answers_for_box['B'])
    
    def test_box_b_correct_answer_fraction(self):
        form = BoxInputForm(data=self.correct_answer_box_b_fraction)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertEqual(form.cleaned_data['user_input'], correct_answers_for_box['B'])

    def test_box_b_correct_answer_fraction_variant(self):
        form = BoxInputForm(data=self.correct_answer_box_b_fraction_variant)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertEqual(form.cleaned_data['user_input'], correct_answers_for_box['B'])
    
    def test_box_b_incorrect_answer_decimal(self):
        form = BoxInputForm(data=self.incorrect_answer_box_a_or_b_decimal)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertNotEqual(form.cleaned_data['user_input'], correct_answers_for_box['B'])
    
    def test_box_b_incorrect_answer_fraction(self):
        form = BoxInputForm(data=self.incorrect_answer_box_a_or_b_fraction)
        # Assert that the form is valid
        self.assertTrue(form.is_valid())
        #Assert that the value is correct
        self.assertNotEqual(form.cleaned_data['user_input'], correct_answers_for_box['B'])
    

    


    

    
