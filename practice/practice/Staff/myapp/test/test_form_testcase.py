from unittest import skip
from django.test import TestCase
from myapp.forms import TaskForm

# @skip("С ошибкой")
# class FormTest(TestCase):
#     def test_form_valid(self):
#         form_data = {'name': 'Парфюмерная вода', 'place': '100', 'price': '7900', 'square': '5'}
#         form = TaskForm(data=form_data)
#         self.assertTrue(form.is_valid())
#
#     # def test_form_invalid(self):
#     #     form_data = {'name': '', 'place': '', 'price': '', 'square': ''}
#     #     form = TaskForm(data=form_data)
#     #     self.assertFalse(form.is_valid())