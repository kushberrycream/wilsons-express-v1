from django.urls import path
from . import views


urlpatterns = [
    path('', views.faqs, name='faqs'),
    path('add/', views.add_faq, name='add_faq'),
    path('edit/<int:q_id>/', views.edit_faq, name='edit_faq'),
    path('delete/<int:q_id>/', views.delete_faq, name='delete_faq'),
]
