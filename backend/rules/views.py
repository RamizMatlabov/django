from django.shortcuts import render, redirect
from .models import Rule
from .forms import RuleForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# CRUD
# - Create
# - Read
# - Update
# - Delete

class RulesView(ListView):
    model = Rule
    template_name = "rules.html"
    context_object_name = "rules"  # defaults to "object_list"




class RulesCreateView(CreateView):
    model = Rule
    form_class = RuleForm  # This lets to use the form that we created inside templates
    template_name = 'create_rule.html'
    success_url = '/rules'

    # set request.user as an author of the post
    def form_valid(self, rule):
        rule.instance.author = self.request.user
        return super().form_valid(rule)



class UpdateRulesView(UpdateView):
    model = Rule
    template_name = 'update_rule.html'
    success_url = '/rules'
    form_class = RuleForm


class RulesDeleteView(DeleteView):
    model = Rule
    template_name = 'post_confirm_delete.html'
    success_url = '/rules'