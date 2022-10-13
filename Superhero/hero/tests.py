from django.test import SimpleTestCase, TestCase

# Create your tests here.
class HeroAppTest(SimpleTestCase):
    
    def test_django(self):
        page = "https://jellyfish-app-w75km.ondigitalocean.app/"
        response = self.client.get(page)
        self.assertEqual(response.status_code, 200)