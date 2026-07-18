from django.shortcuts import render, redirect
from .models import Certificate
from .forms import CertificateForm

def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(request, 'app1/certificate_list.html', {'certificates': certificates})

def certificate_create(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')
    else:
        form = CertificateForm()
    return render(request, 'app1/certificate_form.html', {'form': form})
