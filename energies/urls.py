from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('why-lithium/', views.why_lithium, name='why_lithium'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about, name='about'),
]
