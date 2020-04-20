from django.urls import path
from .views import legal_updates

urlpatterns = [
    path('legal-updates/',legal_updates,name='legal_updates'),

]