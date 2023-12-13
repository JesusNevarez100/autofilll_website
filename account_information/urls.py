from django.urls import path
from . import views

urlpatterns = [
    path('account-information', views.account_information_home, name="Account Information"),
    path('dealership-information', views.dealer_information, name='User Information'),
    path('edit/dealer/<int:dealer_id>/', views.edit_dealer, name='edit_dealer'),
    path('lienholder-information', views.lienholder_information, name='Lienholder Information'),
    path('account-information/edit/lienholder-information/<int:lienholder_id>/', views.edit_lienholder, name='edit_lienholder'),
    path('delete/<int:lienholder_id>/', views.delete_lienholder, name='delete_lienholder'),


    
]