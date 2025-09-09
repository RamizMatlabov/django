# ...existing code...
from django.urls import path
from .views import get_news, create_news, update_news, delete_news

urlpatterns = [
    path('', get_news, name='get_news'),
    path('create/', create_news, name='create_news'),
    path('update/<int:pk>/', update_news, name='update_news'),
    path('delete/<int:pk>/', delete_news, name='delete_news'),
]
# ...existing code...
