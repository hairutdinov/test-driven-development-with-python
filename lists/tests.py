from django.test import TestCase

from lists.models import Item


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        """Тест: используется домашний шаблон"""
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


class ItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """тест сохранения и получения элементов списка"""
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item, second_saved_item = saved_items
        self.assertEqual(first_item.text, "The first (ever) list item")
        self.assertEqual(second_item.text, "Item the second")


class ListViewTest(TestCase):
    """тест представления списка"""

    def test_uses_list_template(self):
        """тест: используется шаблон списка"""
        response = self.client.get("/lists/the-only-list-in-the-world")
        self.assertTemplateUsed(response, "list.html")

    def test_display_all_items(self):
        """тест: отображаются все элементы списка"""
        Item.objects.create(text="itemey 1")
        Item.objects.create(text="itemey 2")

        response = self.client.get("/lists/the-only-list-in-the-world")

        self.assertContains(response, "itemey 1")
        self.assertContains(response, "itemey 2")


class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        """Тест: можно сохранить post-запрос"""
        self.client.post("/lists/new", data={"item_text": "A new list item"})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new list item")

    def test_redirects_after_POST(self):
        """тест: переадресует после post-запроса"""
        response = self.client.post("/lists/new", data={"item_text": "A new list item"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/lists/the-only-list-in-the-world")
