# ...existing code...
from django.urls import path
from .views import *

urlpatterns = [
    path('', RulesView.as_view(), name='get_rules'),
    path('create/', RulesCreateView.as_view(), name='create_rule'),
    path('update/<int:pk>/', UpdateRulesView.as_view(), name='update_rule'),
    path('delete/<int:pk>/', RulesDeleteView.as_view(), name='delete_rule'),
]
# ...existing code...
