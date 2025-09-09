from django.shortcuts import render, redirect
from .models import Rule
from .forms import RuleForm
from django.contrib.auth.decorators import login_required

# CRUD
# - Create
# - Read
# - Update
# - Delete

def get_rules(request):
    context = {
        "rules": Rule.objects.all()
    }
    return render(request, "rules.html", context)

@login_required
def create_rule(request):
    context = { "form": RuleForm() }

    if request.method == "POST":
        form = RuleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('get_rules')

    return render(request, "create_rule.html", context)

@login_required
def update_rule(request, pk: int):
    rule = Rule.objects.get(pk=pk, author=request.user)
    context = {"form": RuleForm(instance=rule)}

    if request.method == "POST":
        form = RuleForm(request.POST, instance=rule)
        if form.is_valid():
            form.save()
            return redirect('get_rules')

    return render(request, "update_rule.html", context)

@login_required
def delete_rule(request, pk: int):
    rule = Rule.objects.get(pk=pk, author=request.user)
    rule.delete()
    return redirect("get_rules")
