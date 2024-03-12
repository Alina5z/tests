from unittest import skip
from django.tests import TestCase
from models import Task


class MyModelTest(TestCase):
    def setUp(self):
        self.object = Task.objects.create(name="Парфюмерия")

    def test_str_representation(self):
        self.assertEqual(str(self.object), 'Парфюмерия')

    def tearDown(self):
        pass