from django.shortcuts import render, redirect
from emails.forms import EmailAccountForm

def email_list_view(request):
    return render(request, 'emails/list.html')

def add_email_account(request):
    if request.method == 'POST':
        form = EmailAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('email_list')
    else:
        form = EmailAccountForm()
    return render(request, 'emails/add_email_account.html', {'form': form})
