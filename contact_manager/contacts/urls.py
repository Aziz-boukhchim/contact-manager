from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list , name="contact_list"),
    path('create/' , views.add_contact, name="create_contact"),
    path('update/<int:pk>/', views.update_contact, name='contact_update'),
    path('delete/<int:pk>/', views.delete_contact, name='contact_delete'),
]
