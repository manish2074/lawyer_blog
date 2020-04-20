from django.urls import path
from .views import home,about,tax_law,corporate_law

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),    
    path('tax-law/',tax_law,name='tax_law'),
    path('corporate-law/',corporate_law,name='corporate_law'), 
]