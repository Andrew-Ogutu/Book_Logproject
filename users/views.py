from django.shortcuts import redirect, render

from django.contrib.auth import logout, login, authenticate

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def Logout_view(request):
    logout(request)
    return redirect(request,'Book_logs:index')

def register(request):
    """ Register a new user"""

    if request.method != 'POST':

        form = UserCreationForm()

    else :
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()

            #Log the user in and then redirect to home page.

            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('Book_logs:index')

    context = {'form': form}
    return render(request, 'register.html', context)


