from django.shortcuts import render, redirect
from . forms import RegisterUserForm


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Login page/feature coming in future
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
