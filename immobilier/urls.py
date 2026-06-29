from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  
from .views import handle_chat_message

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('produit/<int:produit_id>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('produit/<int:produit_id>/upload-zip/', views.upload_zip, name='upload_zip'),
    path('search/', views.smart_search, name='smart_search'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),    
    path('chatbot/', handle_chat_message, name='chatbot_response'),
    path('about/', views.about_view, name='about'),
]