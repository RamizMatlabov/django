# ...existing code...
from django import forms
from .models import Rule

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['title', 'description']
# ...existing code...
