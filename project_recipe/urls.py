from django.contrib import admin
from django.urls import path

from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main_view, name='main'),
    path('recipe_detail/<int:recipe_id>/', views.recipe_detail_view, name='recipe_detail'),
]
