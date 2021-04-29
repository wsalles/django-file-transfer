from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView

from .forms import BookForm, UploadForm
from .models import Book, UploadFiles


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login')


def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Login failed. Invalid user or password.')
    return redirect('/login/')


class Home(TemplateView):
    template_name = 'home.html'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super(Home, self).dispatch(*args, **kwargs)


@login_required(login_url='/login/')
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadForm()

    uploads = UploadFiles.objects.all()
    return render(request, 'upload.html', {
        'uploads': uploads,
        'form': form
    })


@login_required(login_url='/login/')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


@login_required(login_url='/login/')
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


@login_required(login_url='/login/')
def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


@login_required(login_url='/login/')
def delete_files(request, pk):
    if request.method == 'POST':
        uploads = UploadFiles.objects.get(pk=pk)
        uploads.delete()
    return redirect('upload')
