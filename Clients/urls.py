from django.urls import path
from . import views

# Include URL path

urlpatterns = [
    path('client-vault/', views.client_vault, name="Clinet Vault"),
    path('add-client/', views.add_client, name='Add Client'),
    path('edit/client/<int:client_id>/', views.edit_client, name='edit_client'),
    path('delete/client/<int:client_id>/', views.delete_client, name='delete_client'),
]