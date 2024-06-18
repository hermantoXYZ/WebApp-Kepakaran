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
    #Pakar
    # path('daftar-pakar/', viewsDosen.DaftarPakarView.as_view(), name='daftar_pakar'),
    path('bidang/kepakaran/', viewsDosen.BidangKepakaranView, name='bidang_kepakaran'),
    path('pakar/<slug:slug>/', viewsDosen.DetailPakarView.as_view(), name='detail_pakar'),
    path('bidang/kepakaran/<slug:slug>/', viewsDosen.bidang_kepakaran_detail, name='bidang_kepakaran_detail'),
]

