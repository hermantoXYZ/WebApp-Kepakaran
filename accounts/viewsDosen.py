from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.views.generic import ListView, DetailView

from .models import Pakar, BidangKepakaran
from django.shortcuts import render, get_object_or_404



def is_dosen(user):
    return user.is_authenticated and user.is_dosen

@user_passes_test(is_dosen)
def dosen(request):
    return render(request, 'dashboard/dosen.html')

@user_passes_test(is_dosen)
def dashboard_profile(request):
    user = request.user
    return render(request, 'dashboard/profile.html', {'user': user})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'dashboard/profile.html', {'form': form})



# class DaftarPakarView(ListView):
#     model = Pakar
#     template_name = 'kepakaran/daftar_pakar.html'
#     context_object_name = 'pakar_list'

class DetailPakarView(DetailView):
    model = Pakar
    template_name = 'kepakaran/detail_pakar.html'
    context_object_name = 'pakar'

    def get_object(self):
        return Pakar.objects.get(user__username=self.kwargs.get('slug'))


def BidangKepakaranView(request):
    bidang_list = BidangKepakaran.objects.all()
    return render(request, 'kepakaran/bidang_kepakaran_list.html', {'bidang_list': bidang_list})


def bidang_kepakaran_detail(request, slug):
    bidang = get_object_or_404(BidangKepakaran, slug=slug)
    users = bidang.get_users()
    return render(request, 'kepakaran/bidang_kepakaran_detail.html', {'bidang': bidang, 'users': users})

class DetailPakarView(DetailView):
    model = Pakar
    template_name = 'kepakaran/detail_pakar.html'
    context_object_name = 'pakar'
    

    def get_object(self):
        return get_object_or_404(Pakar, user__username=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Dapatkan objek Pakar
        pakar = self.get_object()
        # Tambahkan informasi pengguna ke konteks
        context['user'] = pakar.user
        return context