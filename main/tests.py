from django.test import TestCase, SimpleTestCase

# Create your tests here.
class MainAppTest(SimpleTestCase):
    def test_check_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_home(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_data_home(self):
        response = self.client.get('/data/')
        self.assertEqual(response.status_code, 200)
