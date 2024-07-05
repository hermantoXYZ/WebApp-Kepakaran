from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, PenelitianForm, BookForm, NewsForm, OrganisasiForm, PendidikanForm, PengabdianForm, PakarForm, MinatPenelitianForm
from django.views.generic import ListView, DetailView

from .models import Pakar, BidangKepakaran, Penelitian, Book, InTheNews, Organisasi, Pendidikan, Pengabdian, ProgramStudi
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag


def is_dosen(user):
    return user.is_authenticated and user.is_dosen

@login_required
@user_passes_test(is_dosen)
def dosen(request):
    pakar = get_object_or_404(Pakar, user=request.user)
    total_penelitian = Penelitian.objects.filter(pakar=pakar).count()
    total_buku = Book.objects.filter(pakar=pakar).count()
    total_news = InTheNews.objects.filter(pakar=pakar).count()
    total_pengabdian = Pengabdian.objects.filter(pakar=pakar).count()

    context = {
        'pakar': pakar,
        'total_penelitian': total_penelitian,
        'total_buku': total_buku,
        'total_news': total_news,
        'total_pengabdian': total_pengabdian
    }

    return render(request, 'dashboard/dosen.html', context)



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
    pakar = get_object_or_404(Pakar, user=request.user)
    penelitian_list = Penelitian.objects.filter(pakar=pakar).order_by('-id')
    jumlah_penelitian = penelitian_list.count()
    return render(request, 'dashboard/list_penelitian.html', {'penelitian_list': penelitian_list, 'jumlah_penelitian': jumlah_penelitian})


@login_required
@user_passes_test(is_dosen)
def delete_penelitian(request, penelitian_id):
    penelitian_instance = get_object_or_404(Penelitian, id=penelitian_id)
    if penelitian_instance.pakar.user == request.user:
        if request.method == 'POST':
            penelitian_instance.delete()
            return redirect('list_penelitian')
        else:
            return render(request, 'dashboard/delete/penelitian.html', {'penelitian_instance': penelitian_instance})
    else:
        return HttpResponseForbidden("You are not allowed to delete this object.")


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
    pakar = get_object_or_404(Pakar, user=request.user)
    book_list = Book.objects.filter(pakar=pakar).order_by('-id')
    jumlah_buku = book_list.count()

    return render(request, 'dashboard/list_book.html', {'book_list': book_list, 'jumlah_buku': jumlah_buku})





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
    book_instance = get_object_or_404(Book, id=book_id)
    if book_instance.pakar.user == request.user:
        if request.method == 'POST':
            book_instance.delete()
            return redirect('list_book')
        else:
            return render(request, 'dashboard/delete/book.html', {'book_instance': book_instance})
    else:
        return HttpResponseForbidden("You are not allowed to delete this object.")
    


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
    news_instance = get_object_or_404(InTheNews, id=news_id)
    if news_instance.pakar.user == request.user:
        if request.method == 'POST':
            news_instance.delete()
            return redirect('list_news')
        else:
            return render(request, 'dashboard/delete/news.html', {'news_instance': news_instance})
    else:
        return HttpResponseForbidden("You are not allowed to delete this object.")

@login_required
@user_passes_test(is_dosen)
def list_news(request):
    pakar = get_object_or_404(Pakar, user=request.user)
    news_list = InTheNews.objects.filter(pakar=pakar).order_by('-id')
    jumlah_news = news_list.count()

    # news_list = InTheNews.objects.all().order_by('-id')
    return render(request, 'dashboard/list_news.html', {'news_list': news_list, 'jumlah_news': jumlah_news})






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
    pakar = get_object_or_404(Pakar, user=request.user)
    organisasi_list = Organisasi.objects.filter(pakar=pakar).order_by('-id')
    jumlah_organisasi = organisasi_list.count()
    # organisasi_list = Organisasi.objects.all().order_by('-id')
    return render(request, 'dashboard/list_organisasi.html', {'organisasi_list': organisasi_list, 'jumlah_organisasi': jumlah_organisasi})

@login_required
@user_passes_test(is_dosen)
def delete_organisasi(request, organisasi_id):

    organisasi_instance = get_object_or_404(Organisasi, id=organisasi_id)
    if organisasi_instance.pakar.user == request.user:
        if request.method == 'POST':
            organisasi_instance.delete()
            return redirect('list_organisasi')
        else:
            return render(request, 'dashboard/delete/organisasi.html', {'organisasi_instance': organisasi_instance})
    else:
        return HttpResponseForbidden("You are not allowed to delete this object.")

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
    pakar = get_object_or_404(Pakar, user=request.user)
    pendidikan_list = Pendidikan.objects.filter(pakar=pakar).order_by('-id')
    jumlah_pendidikan = pendidikan_list.count()
    # pendidikan_list = Pendidikan.objects.all().order_by('-id')
    return render(request, 'dashboard/list_pendidikan.html', {'pendidikan_list': pendidikan_list, 'jumlah_pendidikan': jumlah_pendidikan})

@login_required
@user_passes_test(is_dosen)
def delete_pendidikan(request, pendidikan_id):
    pendidikan_instance = get_object_or_404(Pendidikan, id=pendidikan_id)
    if pendidikan_instance.pakar.user == request.user:
        if request.method == 'POST':
            pendidikan_instance.delete()
            return redirect('list_pendidikan')
        else:
            return render(request, 'dashboard/delete/pendidikan.html', {'pendidikan_instance': pendidikan_instance})
    else:
        return HttpResponseForbidden("You are not allowed to delete this object.")



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
    pakar = get_object_or_404(Pakar, user=request.user)
    pengabdian_list = Pengabdian.objects.filter(pakar=pakar).order_by('-id')
    total_pengabdian = pengabdian_list.count()
    # pengabdian_list = Pengabdian.objects.all().order_by('-id').order_by('-id')
    return render(request, 'dashboard/list_pengabdian.html', {'pengabdian_list': pengabdian_list, 'total_pengabdian': total_pengabdian})

@login_required
@user_passes_test(is_dosen)
def delete_pengabdian(request, pengabdian_id):

    pengabdian_instance = get_object_or_404(Pengabdian, id=pengabdian_id)
    if pengabdian_instance.pakar.user == request.user:
        if request.method == 'POST':
            pengabdian_instance.delete()
            return redirect('list_pengabdian')
        else:
            return render(request, 'dashboard/delete/pengabdian.html', {'pengabdian_instance': pengabdian_instance})
    else:
        return HttpResponseForbidden("You are not allowed to delete this object.")
    


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
        pakar_instance = Pakar(user=request.user)

    if request.method == 'POST':
        form = MinatPenelitianForm(request.POST, instance=pakar_instance)
        if form.is_valid():
            pakar_instance = form.save(commit=False)
            pakar_instance.user = request.user
            pakar_instance.save()
            form.save_m2m()
            return redirect('dashboard_dosen')  # Ganti 'dashboard_dosen' dengan URL yang sesuai
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
    program_studi = ProgramStudi.objects.all()
    tags = Tag.objects.all()

    context = {
        'bidang_list': bidang_list,
        'tags': tags,
        'program_studi': program_studi
    }
    return render(request, 'kepakaran/bidang_kepakaran_list.html', context)


def bidang_kepakaran_detail(request, slug):
    bidang = get_object_or_404(BidangKepakaran, slug=slug)
    users = bidang.get_users()
    jumlah_penelitian = Penelitian.objects.filter(pakar__bidang_kepakaran=bidang).count()


    context = {
        'bidang': bidang,
        'users': users,
        'jumlah_penelitian': jumlah_penelitian,
    }

    return render(request, 'kepakaran/bidang_kepakaran_detail.html', context)


def program_studi_detail(request, slug):
    program_studi = get_object_or_404(ProgramStudi, slug=slug)
    users = program_studi.get_users()

    # Menghitung jumlah Pakar dalam Program Studi ini
    total_pakar = program_studi.pakar.count()

    # user_pengabdian_counts = []
    # for user in users:
    #     pengabdian_count = Pengabdian.objects.filter(pakar__user=user).count()
    #     user_pengabdian_counts.append({'user': user, 'total_pengabdian': pengabdian_count})

    # user_penelitian_counts = []
    # for user in users:
    #     penelitian_count = Penelitian.objects.filter(pakar__user=user).count()
    #     user_penelitian_counts.append({'user': user, 'total_penelitian': penelitian_count})


    return render(request, 'kepakaran/program_studi_detail.html', {
        'program_studi': program_studi,
        'users': users,
        'total_pakar': total_pakar,
        # 'user_pengabdian_counts': user_pengabdian_counts,
        # 'user_penelitian_counts': user_penelitian_counts
  
    })

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
    
def users_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    users = Pakar.objects.filter(tags__name__in=[tag.name])
    program_studi = ProgramStudi.objects.all()  # Ambil semua program studi
    
    context = {
        'tag': tag,
        'users': users,
        'program_studi': program_studi,  # Tambahkan program studi ke konteks
    }
    return render(request, 'kepakaran/users_by_tag.html', context)



