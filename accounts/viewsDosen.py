from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, PenelitianForm, BookForm, NewsForm, OrganisasiForm, PendidikanForm, PengabdianForm, PakarForm, MinatPenelitianForm
from django.views.generic import ListView, DetailView

from .models import Pakar, BidangKepakaran, Penelitian, Book, InTheNews, Organisasi, Pendidikan, Pengabdian
from django.shortcuts import render, get_object_or_404



def is_dosen(user):
    return user.is_authenticated and user.is_dosen

@login_required
@user_passes_test(is_dosen)
def dosen(request):
    return render(request, 'dashboard/dosen.html')

@login_required
@user_passes_test(is_dosen)
def dashboard_profile(request):
    user = request.user
    return render(request, 'dashboard/profile.html', {'user': user})

@login_required
@user_passes_test(lambda u: u.is_dosen)
def penelitian(request):
    user_pakar = request.user.pakar  # Mengambil objek Pakar terkait dengan User yang sedang login

    if request.method == 'POST':
        form_penelitian = PenelitianForm(request.POST, request.FILES)
        if form_penelitian.is_valid():
            penelitian_instance = form_penelitian.save(commit=False)
            penelitian_instance.pakar = user_pakar  # Set pakar ke pakar yang terkait dengan user yang sedang login
            penelitian_instance.save()
            return redirect('list_penelitian')  # Ganti dengan nama URL dashboard dosen
    else:
        form_penelitian = PenelitianForm()

    context = {
        'form_penelitian': form_penelitian
    }

    return render(request, 'dashboard/penelitian.html', context)

@login_required
@user_passes_test(lambda u: u.is_dosen)
def edit_penelitian(request, penelitian_id):
    penelitian_instance = get_object_or_404(Penelitian, id=penelitian_id)
    user_pakar = request.user.pakar  # Mengambil objek Pakar terkait dengan User yang sedang login

    if request.method == 'POST':
        form_penelitian = PenelitianForm(request.POST, request.FILES, instance=penelitian_instance)
        if form_penelitian.is_valid():
            penelitian_instance = form_penelitian.save(commit=False)
            penelitian_instance.pakar = user_pakar  # Set pakar ke pakar yang terkait dengan user yang sedang login
            penelitian_instance.save()
            return redirect('list_penelitian')  # Ganti dengan nama URL dashboard dosen
    else:
        form_penelitian = PenelitianForm(instance=penelitian_instance)

    context = {
        'form_penelitian': form_penelitian,
        'penelitian_id': penelitian_id,
    }

    return render(request, 'dashboard/edit_penelitian.html', context)

@login_required
@user_passes_test(is_dosen)
def list_penelitian(request):
    try:
        pakar = Pakar.objects.get(user=request.user)
        penelitian_list = Penelitian.objects.filter(pakar=pakar).order_by('-id')
        return render(request, 'dashboard/list_penelitian.html', {'penelitian_list': penelitian_list})
    except Pakar.DoesNotExist:
        penelitian_list = []
    
    return render(request, 'dashboard/list_penelitian.html', {'penelitian_list': penelitian_list})
@login_required
@user_passes_test(is_dosen)
def delete_penelitian(request, penelitian_id):
    penelitian_instance = get_object_or_404(Penelitian, id=penelitian_id)
    penelitian_instance.delete()
    return redirect('list_penelitian')





@login_required
@user_passes_test(lambda u: u.is_dosen)
def book(request):
    user_pakar = request.user.pakar  # Mengambil objek Pakar terkait dengan User yang sedang login

    if request.method == 'POST':
        form_book= BookForm(request.POST, request.FILES)
        if form_book.is_valid():
            penelitian_instance = form_book.save(commit=False)
            penelitian_instance.pakar = user_pakar  # Set pakar ke pakar yang terkait dengan user yang sedang login
            penelitian_instance.save()
            return redirect('list_book')  # Ganti dengan nama URL dashboard dosen
    else:
        form_book = BookForm()

    context = {
        'form_book': form_book
    }

    return render(request, 'dashboard/book.html', context)


@login_required
@user_passes_test(is_dosen)
def list_buku(request):
    book_list = Book.objects.all().order_by('-id')
    return render(request, 'dashboard/list_book.html', {'book_list': book_list})

@login_required
@user_passes_test(lambda u: u.is_dosen)
def edit_book(request, book_id):
    penelitian_instance = get_object_or_404(Book, id=book_id)
    user_pakar = request.user.pakar  # Mengambil objek Pakar terkait dengan User yang sedang login

    if request.method == 'POST':
        form_book = BookForm(request.POST, request.FILES, instance=penelitian_instance)
        if form_book.is_valid():
            penelitian_instance = form_book.save(commit=False)
            penelitian_instance.pakar = user_pakar  # Set pakar ke pakar yang terkait dengan user yang sedang login
            penelitian_instance.save()
            return redirect('list_book')  # Ganti dengan nama URL dashboard dosen
    else:
        form_book = BookForm(instance=penelitian_instance)

    context = {
        'form_book': form_book,
        'book_id': book_id,
    }

    return render(request, 'dashboard/edit_book.html', context)


@login_required
@user_passes_test(is_dosen)
def delete_book(request, book_id):
    penelitian_instance = get_object_or_404(Book, id=book_id)
    penelitian_instance.delete()
    return redirect('list_book')




@login_required
@user_passes_test(lambda u: u.is_dosen)
def news(request):
    user_pakar = request.user.pakar  # Mengambil objek Pakar terkait dengan User yang sedang login

    if request.method == 'POST':
        form_news= NewsForm(request.POST, request.FILES)
        if form_news.is_valid():
            penelitian_instance = form_news.save(commit=False)
            penelitian_instance.pakar = user_pakar  # Set pakar ke pakar yang terkait dengan user yang sedang login
            penelitian_instance.save()
            return redirect('list_news')  # Ganti dengan nama URL dashboard dosen
        
        else:
            print(form_news.errors)
    else:
        form_news = NewsForm()


    context = {
        'form_news': form_news
    }

    return render(request, 'dashboard/news.html', context)

@login_required
@user_passes_test(is_dosen)
def delete_news(request, news_id):
    penelitian_instance = get_object_or_404(InTheNews, id=news_id)
    penelitian_instance.delete()
    return redirect('list_news')

@login_required
@user_passes_test(is_dosen)
def list_news(request):
    news_list = InTheNews.objects.all().order_by('-id')
    return render(request, 'dashboard/list_news.html', {'news_list': news_list})

@login_required
@user_passes_test(lambda u: u.is_dosen)
def edit_news(request, news_id):
    penelitian_instance = get_object_or_404(InTheNews, id=news_id)
    user_pakar = request.user.pakar  # Mengambil objek Pakar terkait dengan User yang sedang login

    if request.method == 'POST':
        form_news = NewsForm(request.POST, request.FILES, instance=penelitian_instance)
        if form_news.is_valid():
            penelitian_instance = form_news.save(commit=False)
            penelitian_instance.pakar = user_pakar  # Set pakar ke pakar yang terkait dengan user yang sedang login
            penelitian_instance.save()
            return redirect('list_news')  # Ganti dengan nama URL dashboard dosen
    else:
        form_news = NewsForm(instance=penelitian_instance)

    context = {
        'form_news': form_news,
        'news_id': news_id,
    }

    return render(request, 'dashboard/edit_news.html', context)




@login_required
@user_passes_test(lambda u: u.is_dosen)
def organisasi(request):
    user_pakar = request.user.pakar  # Mengambil objek Pakar terkait dengan User yang sedang login

    if request.method == 'POST':
        form_organisasi= OrganisasiForm(request.POST, request.FILES)
        if form_organisasi.is_valid():
            penelitian_instance = form_organisasi.save(commit=False)
            penelitian_instance.pakar = user_pakar  # Set pakar ke pakar yang terkait dengan user yang sedang login
            penelitian_instance.save()
            return redirect('list_organisasi')  # Ganti dengan nama URL dashboard dosen
        
        else:
            print(form_organisasi.errors)
    else:
        form_organisasi = OrganisasiForm()


    context = {
        'form_organisasi': form_organisasi
    }

    return render(request, 'dashboard/organisasi.html', context)


@login_required
@user_passes_test(lambda u: u.is_dosen)
def edit_organisasi(request, organisasi_id):
    penelitian_instance = get_object_or_404(Organisasi, id=organisasi_id)
    user_pakar = request.user.pakar  # Mengambil objek Pakar terkait dengan User yang sedang login

    if request.method == 'POST':
        form_organisasi = OrganisasiForm(request.POST, request.FILES, instance=penelitian_instance)
        if form_organisasi.is_valid():
            penelitian_instance = form_organisasi.save(commit=False)
            penelitian_instance.pakar = user_pakar  # Set pakar ke pakar yang terkait dengan user yang sedang login
            penelitian_instance.save()
            return redirect('list_organisasi')  # Ganti dengan nama URL dashboard dosen
    else:
        form_organisasi = OrganisasiForm(instance=penelitian_instance)

    context = {
        'form_organisasi': form_organisasi,
        'organisasi_id': organisasi_id,
    }

    return render(request, 'dashboard/edit_organisasi.html', context)

@login_required
@user_passes_test(is_dosen)
def list_organisasi(request):
    organisasi_list = Organisasi.objects.all().order_by('-id')
    return render(request, 'dashboard/list_organisasi.html', {'organisasi_list': organisasi_list})

@login_required
@user_passes_test(is_dosen)
def delete_organisasi(request, organisasi_id):
    penelitian_instance = get_object_or_404(Organisasi, id=organisasi_id)
    penelitian_instance.delete()
    return redirect('list_organisasi')



@login_required
@user_passes_test(lambda u: u.is_dosen)
def pendidikan(request):
    user_pakar = request.user.pakar

    if request.method == 'POST':
        form_pendidikan = PendidikanForm(request.POST, request.FILES)
        if form_pendidikan.is_valid():
            penelitian_instance = form_pendidikan.save(commit=False)
            penelitian_instance.pakar = user_pakar
            penelitian_instance.save()
            return redirect('list_pendidikan')

    else:
        form_pendidikan = PendidikanForm()

    context = {
        'form_pendidikan': form_pendidikan
    }

    return render(request, 'dashboard/pendidikan.html', context)


@login_required
@user_passes_test(lambda u: u.is_dosen)
def edit_pendidikan(request, pendidikan_id):
    penelitian_instance = get_object_or_404(Pendidikan, id=pendidikan_id)
    user_pakar = request.user.pakar

    if request.method == 'POST':
        form_pendidikan = PendidikanForm(request.POST, request.FILES, instance=penelitian_instance)
        if form_pendidikan.is_valid():
            penelitian_instance = form_pendidikan.save(commit=False)
            penelitian_instance.pakar = user_pakar
            penelitian_instance.save()
            return redirect('list_pendidikan')

    else:
        form_pendidikan = PendidikanForm(instance=penelitian_instance)

    context = {
        'form_pendidikan': form_pendidikan,
        'pendidikan_id': pendidikan_id,
    }

    return render(request, 'dashboard/edit_pendidikan.html', context)

@login_required
@user_passes_test(is_dosen)
def list_pendidikan(request):
    pendidikan_list = Pendidikan.objects.all().order_by('-id')
    return render(request, 'dashboard/list_pendidikan.html', {'pendidikan_list': pendidikan_list})

@login_required
@user_passes_test(is_dosen)
def delete_pendidikan(request, pendidikan_id):
    penelitian_instance = get_object_or_404(Pendidikan, id=pendidikan_id)
    penelitian_instance.delete()
    return redirect('list_pendidikan')

@login_required
@user_passes_test(lambda u: u.is_dosen)
def pengabdian(request):
    user_pakar = request.user.pakar

    if request.method == 'POST':
        form_pengabdian = PengabdianForm(request.POST, request.FILES)
        if form_pengabdian.is_valid():
            penelitian_instance = form_pengabdian.save(commit=False)
            penelitian_instance.pakar = user_pakar
            penelitian_instance.save()
            return redirect('list_pengabdian')
        else:
            print(form_pengabdian.errors)

    else:
        form_pengabdian = PengabdianForm()

    context = {
        'form_pengabdian': form_pengabdian
    }

    return render(request, 'dashboard/pengabdian.html', context)

@login_required
@user_passes_test(is_dosen)
def list_pengabdian(request):
    pengabdian_list = Pengabdian.objects.all().order_by('-id').order_by('-id')
    return render(request, 'dashboard/list_pengabdian.html', {'pengabdian_list': pengabdian_list})

@login_required
@user_passes_test(is_dosen)
def delete_pengabdian(request, pengabdian_id):
    penelitian_instance = get_object_or_404(Pengabdian, id=pengabdian_id)
    penelitian_instance.delete()
    return redirect('list_pengabdian')


@login_required
@user_passes_test(lambda u: u.is_dosen)
def edit_pengabdian(request, pengabdian_id):
    penelitian_instance = get_object_or_404(Pengabdian, id=pengabdian_id)
    user_pakar = request.user.pakar

    if request.method == 'POST':
        form_pengabdian = PengabdianForm(request.POST, request.FILES, instance=penelitian_instance)
        if form_pengabdian.is_valid():
            penelitian_instance = form_pengabdian.save(commit=False)
            penelitian_instance.pakar = user_pakar
            penelitian_instance.save()
            return redirect('list_pengabdian')
        else:
            print(form_pengabdian.errors)

    else:
        form_pengabdian = PengabdianForm(instance=penelitian_instance)

    context = {
        'form_pengabdian': form_pengabdian,
        'pengabdian_id': pengabdian_id,
    }

    return render(request, 'dashboard/edit_pengabdian.html', context)   

@login_required
@user_passes_test(is_dosen)
@login_required
def bidang_pakar (request):
    dosen = request.user.pakar
    if request.method == 'POST':
        form = PakarForm(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            return redirect('dashboard_dosen')  # Ganti dengan nama rute dashboard dosen Anda
    else:
        form = PakarForm(instance=dosen)
    
    return render(request, 'dashboard/bidang_kepakaran.html', {'form': form})

@user_passes_test(is_dosen)
@login_required
def bidang_minat(request):
    try:
        pakar_instance = Pakar.objects.get(user=request.user)
    except Pakar.DoesNotExist:
        pakar_instance = None

    if request.method == 'POST':
        form = MinatPenelitianForm(request.POST, instance=pakar_instance)
        if form.is_valid():
            pakar_instance = form.save(commit=False)
            pakar_instance.user = request.user
            pakar_instance.save()
            form.save_m2m()
            return redirect('dashboard_dosen')  # Ganti 'success_url' dengan URL yang sesuai
    else:
        form = MinatPenelitianForm(instance=pakar_instance)

    return render(request, 'dashboard/bidang_peminatan.html', {'form': form})



@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard_dosen')
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
        context['tags'] = pakar.tags.all()
        return context