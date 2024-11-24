from django.shortcuts import render, get_object_or_404, redirect
from .models import GrantApplication
from .forms import GrantApplicationForm

# View for submitting an application


def submit_application(request):
    if request.method == 'POST':
        form = GrantApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_list')
    else:
        form = GrantApplicationForm()
    return render(request, 'applications/submit_application.html', {'form': form})

# View for listing all applications


def application_list(request):
    applications = GrantApplication.objects.all()
    return render(request, 'applications/application_list.html', {'applications': applications})

# View for viewing a single application


def application_detail(request, pk):
    application = get_object_or_404(GrantApplication, pk=pk)
    return render(request, 'applications/application_detail.html', {'application': application})
