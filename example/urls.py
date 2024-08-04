from django.urls import path
from .views import NewsView 

urlpatterns = [
    path('api/news/', NewsView.as_view(), name='news'),
]
