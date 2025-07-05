from django.shortcuts import render


def rules_page(request):
    return render(request, 'rules/rules.html')
