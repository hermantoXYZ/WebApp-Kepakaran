from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView

from .models import PostNews, Page, BidangKepakaran, ProgramStudi, Pakar
from taggit.models import Tag

from django.db.models import Q
from .forms import SearchForm


class CustomPasswordResetView(PasswordResetView):
    success_url = '/accounts/reset/password/done/'
    email_template_name = 'accounts/custom_password_reset_email.html'


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('dashboard_admin')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('dashboard_staff')
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('dashboard_user')
            elif user is not None and user.is_dosen:
                login(request, user)
                return redirect('dashboard_dosen')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')  # Redirect to your desired page after signup
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})

# Logout View

def logout_view(request):
    logout(request)
    return redirect('login')

# @login_required
# def dashboard_view(request):
#     # Your dashboard logic goes here
#     return render(request, 'dashboard.html')



def index(request):
    news_list = PostNews.objects.all()
    bidang_list = BidangKepakaran.objects.all()
    program_studi = ProgramStudi.objects.all()
    tags = Tag.objects.all()

    context = {
        'news_list': news_list,
        'bidang_list': bidang_list,
        'tags': tags,
        'program_studi': program_studi
    }
    return render(request, 'home/index.html', context)

def news_detail(request, slug):
    news = get_object_or_404(PostNews, slug=slug)
    context = {
        'news': news
    }
    return render(request, 'home/news_detail.html', context)


def page_detail (request, slug):
    page = get_object_or_404(Page, slug=slug)
    context = {
        'page': page
    }
    return render(request, 'home/page_detail.html', context)



def search(request):
    form = SearchForm()
    query = None
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Pakar.objects.filter(
                Q(user__username__icontains=query) |
                Q(bidang_kepakaran__nama_bidang__icontains=query) |
                Q(program_studi__nama_program__icontains=query) |
                Q(tags__name__icontains=query)
            ).exclude(user__username='admin').distinct()
    return render(request, 'home/search_results.html', {'form': form, 'query': query, 'results': results})