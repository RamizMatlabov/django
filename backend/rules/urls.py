# ...existing code...
from django.urls import path
from .views import get_rules, create_rule, update_rule, delete_rule

urlpatterns = [
    path('', get_rules, name='get_rules'),
    path('create/', create_rule, name='create_rule'),
    path('update/<int:pk>/', update_rule, name='update_rule'),
    path('delete/<int:pk>/', delete_rule, name='delete_rule'),
]
# ...existing code...
