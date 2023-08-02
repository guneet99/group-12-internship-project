from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from blog.emailSender import emailSender

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            save_it=form.save(commit=False)
            save_it.save()

            # form.save()
            emaill = form.cleaned_data.get('email')
            mail_message="Your Account has been created sucessfully. Welcome to FitZone community"
            subject= "Registration Completed Sucessfully"
            # emailSender(emaill,mail_message,subject)

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register1.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
                                   
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            upd_username=request.POST.get('username')
            upd_email=request.POST.get('email')

            mail_message="Your Account has been updated sucessfully. Your Username is "+ upd_username + "and email address is " + upd_email + ". Thanks for connecting. Regards FitZone community"
            subject= "Profile Updated Sucessfully"
            # emailSender(upd_email,mail_message,subject)

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
