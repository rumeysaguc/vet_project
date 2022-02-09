from allauth.account.forms import UserForm, LoginForm, SignupForm
from allauth.account.views import logout
# from allauth.socialaccount.forms import SignupForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext


from animal.models import Animal



def main(request):
    animals = Animal.objects.all()
    form = LoginForm()
    return render(request, "index.html", {'animals': animals, 'form': form})


def signup_page(request):
    return render(request, "signup.html")


from django.contrib.auth import login, authenticate  # add to imports


def login_user(request):
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render('login.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})
