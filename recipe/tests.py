from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Recipe

class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_url(self):
        # Test that the main url resolves to the main view
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_recipe_detail_url(self):
        # Test that the recipe detail url resolves to the recipe detail view
        # Create a dummy category and recipe for testing
        category = Category.objects.create(name='Test')
        recipe = Recipe.objects.create(title='Test Recipe', description='Test Description', instructions='Test Instructions', ingredients='Test Ingredients', category=category)
        response = self.client.get(reverse('recipe_detail', args=[recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some dummy categories and recipes for testing
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')
        self.recipe1 = Recipe.objects.create(title='Recipe 1', description='Description 1',
                                             instructions='Instructions 1', ingredients='Ingredients 1',
                                             category=self.category1)
        self.recipe2 = Recipe.objects.create(title='Recipe 2', description='Description 2',
                                             instructions='Instructions 2', ingredients='Ingredients 2',
                                             category=self.category2)
    def test_main_view(self):
        # Test that the main view returns all recipes for the current year
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        # Check that the context contains only the recipes for the current year
        recipes = response.context['recipes']
        self.assertIn(self.recipe1, recipes)
        self.assertIn(self.recipe2, recipes)

    def test_recipe_detail_view(self):
        # Test that the recipe detail view returns the correct recipe by id
        response = self.client.get(reverse('recipe_detail', args=[self.recipe1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')
        # Check that the context contains the correct recipe
        recipe = response.context['recipe']
        self.assertEqual(recipe, self.recipe1)