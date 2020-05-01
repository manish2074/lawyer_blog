from django.urls import path
from .views import legal_updates,legal_detail,event_detail

urlpatterns = [
    path('legal-updates/',legal_updates,name='legal_updates'),
    path('legal-detail/<str:slug>/<int:pk>/',legal_detail,name='legal_detail'),
    path('event-detail/<str:slug>/<int:pk>/',event_detail,name='event_detail'),

]