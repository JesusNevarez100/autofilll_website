from django.urls import path
from . import views

urlpatterns = [
    path('upload-pdf/', views.upload_pdf, name='upload_pdf'),
    path('edit-pdf/', views.edit_pdf, name='edit_pdf'),

]


