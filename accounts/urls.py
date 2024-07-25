# accounts/urls.py

from django.urls import path
from . import views, viewsAdmin, viewsStaff, viewsUser, viewsDosen
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register', views.signup_view, name='register'),
    path('logout', views.logout_view, name='logout'),

    path('', views.index, name= 'index'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),

    #Reset Password
    path('accounts/password/reset/', CustomPasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('accounts/reset/password/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    #Admin
    path('dashboard/admin', viewsAdmin.admin, name='dashboard_admin'),
    #Pelanggan
    path('dashboard/staff', viewsStaff.staff, name='dashboard_staff'),
    #User
    path('dashboard/user', viewsUser.user, name='dashboard_user'),
    #Dosen
    path('dashboard/dosen', viewsDosen.dosen, name='dashboard_dosen'),
    path('dashboard/profile/', viewsDosen.dashboard_profile, name='profile'),
    path('dashboard/profile/update', viewsDosen.update_profile, name='update_profile'),
    #Dosen Penelitian
    path('dashboard/dosen/penelitian', viewsDosen.penelitian, name='add_penelitian'),
    path('dashboard/dosen/list/penelitian', viewsDosen.list_penelitian, name='list_penelitian'),
    path('dashboard/dosen/<int:penelitian_id>/edit/', viewsDosen.edit_penelitian, name='edit_penelitian'),
    path('dashboard/dosen/<int:penelitian_id>/delete/', viewsDosen.delete_penelitian, name='delete_penelitian'),
    #Dosen Buku
    path('dashboard/dosen/buku', viewsDosen.book, name='add_book'),
    path('dashboard/dosen/list/buku', viewsDosen.list_buku, name='list_book'),
    path('dashboard/dosen/book/<int:book_id>/edit/', viewsDosen.edit_book, name='edit_book'),
    path('dashboard/dosen/book/<int:book_id>/delete/', viewsDosen.delete_book, name='delete_book'),
    #Dosen News
    path('dashboard/dosen/news', viewsDosen.news, name='add_news'),
    path('dashboard/dosen/list/news', viewsDosen.list_news, name='list_news'),
    path('dashboard/dosen/news/<int:news_id>/edit/', viewsDosen.edit_news, name='edit_news'),
    path('dashboard/dosen/news/<int:news_id>/delete/', viewsDosen.delete_news, name='delete_news'),
    #Dosen organisasi
    path('dashboard/dosen/organisasi', viewsDosen.organisasi, name='add_organisasi'),
    path('dashboard/dosen/list/organisasi', viewsDosen.list_organisasi, name='list_organisasi'),
    path('dashboard/dosen/organisasi/<int:organisasi_id>/edit/', viewsDosen.edit_organisasi, name='edit_organisasi'),
    path('dashboard/dosen/organisasi/<int:organisasi_id>/delete/', viewsDosen.delete_organisasi, name='delete_organisasi'),
    #Dosen Pendidikan
    path('dashboard/dosen/pendidikan', viewsDosen.pendidikan, name='add_pendidikan'),
    path('dashboard/dosen/list/pendidikan', viewsDosen.list_pendidikan, name='list_pendidikan'),
    path('dashboard/dosen/pendidikan/<int:pendidikan_id>/edit/', viewsDosen.edit_pendidikan, name='edit_pendidikan'),
    path('dashboard/dosen/pendidikan/<int:pendidikan_id>/delete/', viewsDosen.delete_pendidikan, name='delete_pendidikan'),
    #Dosen Pengabdian
    path('dashboard/dosen/pengabdian', viewsDosen.pengabdian, name='add_pengabdian'),
    path('dashboard/dosen/list/pengabdian', viewsDosen.list_pengabdian, name='list_pengabdian'),
    path('dashboard/dosen/pengabdian/<int:pengabdian_id>/edit/', viewsDosen.edit_pengabdian, name='edit_pengabdian'),
    path('dashboard/dosen/pengabdian/<int:pengabdian_id>/delete/', viewsDosen.delete_pengabdian, name='delete_pengabdian'),
    #Dosen Kepakaran
    path('dashboard/dosen/kepakaran', viewsDosen.bidang_pakar, name='add_kepakaran'),
    path('dashboard/dosen/peminatan', viewsDosen.bidang_minat, name='add_peminatan'),


    #Pakar
    # path('daftar-pakar/', viewsDosen.DaftarPakarView.as_view(), name='daftar_pakar'),
    path('bidang/kepakaran/', viewsDosen.BidangKepakaranView, name='bidang_kepakaran'),
    path('program-studi/', viewsDosen.program_studi_list, name='program_studi'),
    path('minat-penelitian/', viewsDosen.minat_penelitian_list, name='minat_penelitian'),
    path('tags/<slug:tag_slug>/', viewsDosen.users_by_tag, name='users_by_tag'),
    path('pakar/<slug:slug>/', viewsDosen.DetailPakarView.as_view(), name='detail_pakar'),
    path('bidang/kepakaran/<slug:slug>/', viewsDosen.bidang_kepakaran_detail, name='bidang_kepakaran_detail'),
    path('bidang/program-studi/<slug:slug>/', viewsDosen.program_studi_detail, name='program_studi_detail'),

    path('search/', views.search, name='search'),
]

