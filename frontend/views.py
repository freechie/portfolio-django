from django.shortcuts import redirect, render


def index(request):
    return render(request, 'frontend/index.html')


def legacy_index(request):
    return redirect('project_index', permanent=True)
