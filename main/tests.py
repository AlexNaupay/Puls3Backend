from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class SimpleTest(TestCase):
	def test_home(self):
		res = self.client.get('/')
		self.assertEqual(res.status_code,200)
		res = self.client.get(reverse('home'))
		self.assertEqual(res.status_code,200)
		res = self.client.get(reverse('home2'))
		self.assertEqual(res.status_code,200)
