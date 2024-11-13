from django.urls import path
from LatestApp import views


urlpatterns = [
        path('index/', views.index, name='index'),
        path('add_categories/', views.add_categories, name='add_categories'),
        path('save_categories/', views.save_categories, name='save_categories'),
        path('display_categories/', views.display_categories, name='display_categories'),


        path('edit_categories/<int:cat_id>/', views.edit_categories, name='edit_categories'),
        path('update_categories/<int:cat_id>/', views.update_categories, name='update_categories'),
        path('delete_categories/<int:cat_id>/', views.delete_categories, name='delete_categories'),


        path('add_products/', views.add_products, name='add_products'),
        path('save_products/', views.save_products, name='save_products'),
        path('display_products/', views.display_products, name='display_products'),


        path('edit_products/<int:pro_id>/', views.edit_products, name='edit_products'),
        path('update_products/<int:pro_id>/', views.update_products, name='update_products'),
        path('delete_products/<int:pro_id>/', views.delete_products, name='delete_products'),

]
