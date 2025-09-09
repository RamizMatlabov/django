# ...existing code...
from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name='get_news'),
    path('create/', NewsCreateView.as_view(), name='create_news'),
    path('update/<int:pk>/', UpdateNewsView.as_view(), name='update_news'),
    path('delete/<int:pk>/', NewsDeleteView.as_view(), name='delete_news'),
]
# ...existing code...
