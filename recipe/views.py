from django.shortcuts import render, get_object_or_404
from .models import Recipe

def main_view(request):
    # Отримати всі рецепти за 2023 рік
    recipes = Recipe.objects.filter(created_at__year=2023)
    context = {'recipes': recipes}
    return render(request, 'main.html', context)

def recipe_detail_view(request, recipe_id):
    # Отримати певний рецепт за його id
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipe_detail.html', context)

