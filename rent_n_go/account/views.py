from django.shortcuts import render, redirect ,reverse
from .forms import SignUpForm, LoginForm,EventForm
from django.contrib.auth import authenticate, login ,logout
from .models import DateModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)


            if user is not None and user.is_customer:
                login(request, user)
                return redirect('booknow')
            elif user is not None and user.is_host:
                login(request, user)
                return redirect('host')
            else:
                messages.error(request,"User doesnot exist..!")
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


@login_required
def dateandtime(request):
    if request.method == 'POST':
        form = EventForm(request.POST,user=request.user)
        if form.is_valid():
            user=form.save(commit=False)
            user.user = request.user
            user.save()
            if user.is_car:
                return redirect('cars')
            if user.is_bike:
                return redirect('bikes')
    else:
        form = EventForm()

    return render(request, 'dateandtime.html', {'form': form})

@login_required
def cars(request):
    return render(request,'cars.html')

@login_required
def bikes(request):
    return render(request,'bikes.html')

@login_required
def customer(request):
    return render(request,'booknow.html')

@login_required
def host(request):
    return render(request,'host.html')
@login_required
def pay1(request):
    return render(request,'pay1.html')
@login_required
def pay2(request):
    return render(request,'pay2.html')
@login_required
def pay3(request):
    return render(request,'pay3.html')
@login_required
def pay4(request):
    return render(request,'pay4.html')
@login_required
def pay5(request):
    return render(request,'pay5.html')
@login_required
def pay6(request):
    return render(request,'pay6.html')
@login_required
def pay7(request):
    return render(request,'pay7.html')
@login_required
def pay8(request):
    return render(request,'pay8.html')
@login_required
def pay9(request):
    return render(request,'pay9.html')
@login_required
def pay10(request):
    return render(request,'pay10.html')
@login_required
def pay11(request):
    return render(request,'pay11.html')
@login_required
def pay12(request):
    return render(request,'pay12.html')
@login_required
def pay13(request):
    return render(request,'pay13.html')
@login_required
def pay14(request):
    return render(request,'pay14.html')
@login_required
def pay15(request):
    return render(request,'pay15.html')
@login_required
def pay16(request):
    return render(request,'pay16.html')
@login_required
def pay17(request):
    return render(request,'pay17.html')
@login_required
def pay18(request):
    return render(request,'pay18.html')
@login_required
def pay19(request):
    return render(request,'pay19.html')
@login_required
def pay20(request):
    return render(request,'pay20.html')
@login_required
def success(request):
    return render(request,'success.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))
@login_required
def hostadd(request):
    return render(request,'host1.html')
@login_required
def added(request):
    return render(request,'host2.html')
