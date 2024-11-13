from django.urls import path
from StoreApp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('save_signup/', views.save_signup, name='save_signup'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('products_filtered/<pro_id>/', views.products_filtered, name='products_filtered'),
    path('single_product/<int:pro_id>/', views.single_product, name='single_product'),

]