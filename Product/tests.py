from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.

class ViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		prod = Products.objects.create(name = "Kierownica", count = 1)
		prod.save()
		prod = Products.objects.create(name = "Łożysko", count = 2)
		prod.save()
		user = User.objects.create_user(username = "test", email = "lol@o2.pl", password = "test123")

	def test_prod_fullname(self):
		prod = Products.objects.create(name = "Śruba 0.5mm", count = 5)
		self.assertEqual("Śruba 0.5mm[5]", prod.fullname)

	def test_home(self):
		response = self.client.get('/')
		self.assertContains(response, "Magazyn SiloAdmin 1.0.0.!", 1, 200)

	def test_prod_not_exist(self):
		response = self.client.get('/prod_edit/100')
		self.assertEqual(response.status_code, 404)

	def test_prod_edit(self):
		prod = Products.objects.all().filter(count = 1)
		self.assertEqual(prod[0].name, "Kierownica")
		self.assertEqual(prod[0].id, 1)
		response = self.client.get('/prod_edit/6')
		self.assertContains(response, "Kierownica[1]", 1, 404)

	def test_nodata(self):
		with self.assertRaises(IndexError):
			Products.objects.all().filter(count = 123)[0]