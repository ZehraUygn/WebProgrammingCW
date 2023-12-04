from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm

def main_spa(request: HttpRequest) -> HttpResponse:
    show_signup_section = True

    if not show_signup_section:
        return redirect('login')

    return render(request, 'api/spa/index.html', {'show_signup_section': show_signup_section})

def SignUpView(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'api/spa/index.html', context)

def LogInView(request):
    return render(request, 'api/spa/index.html', {})
