from django.test import TestCase

# Create your tests here.


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        """Тест: используется домашний шаблон"""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
