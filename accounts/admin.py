from django.contrib import admin
from .models import User, PostNews, Category, Page
from tinymce.widgets import TinyMCE
from django.db import models
from tinymce.models import HTMLField

# Register your models here.

from .models import BidangKepakaran, Pakar, Pendidikan, Penelitian, InTheNews, Pengabdian, Organisasi, Book, ProgramStudi

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'email', 'no_hp', 'social_media_ig', 'social_media_twitter', 'social_media_facebook')
#     search_fields = ('user__username', 'email', 'no_hp')

class BidangKepakaranAdmin(admin.ModelAdmin):
    list_display = ('nama_bidang', 'slug')
    search_fields = ('nama_bidang',)
    prepopulated_fields = {'slug': ('nama_bidang',)}

class PendidikanInline(admin.TabularInline):
    model = Pendidikan
    extra = 1

# class PublikasiInline(admin.TabularInline):
#     model = Publikasi
#     extra = 1

class PenelitianInline(admin.TabularInline):
    model = Penelitian
    extra = 1

# class RiwayatPenelitianInline(admin.TabularInline):
#     model = RiwayatPenelitian
#     extra = 1

class InTheNewsInline(admin.TabularInline):
    model = InTheNews
    extra = 1


class PengabdianInline(admin.TabularInline):
    model = Pengabdian
    extra = 1

class OrganisasiInline(admin.TabularInline):
    model = Organisasi
    extra = 1


class BookInline(admin.TabularInline):
    model = Book
    extra = 1


class PakarAdmin(admin.ModelAdmin):
    list_display = ('user',  'get_bidang_kepakaran', 'program_studi')
    inlines = [PendidikanInline, PengabdianInline, OrganisasiInline, BookInline, PenelitianInline, InTheNewsInline]
    filter_horizontal = ('bidang_kepakaran',)
    list_filter = ('user', 'bidang_kepakaran', 'program_studi')
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'bidang_kepakaran__nama_bidang', 'program_studi__nama_program', 'tags__name']

    def get_bidang_kepakaran(self, obj):
        return ", ".join([bk.nama_bidang for bk in obj.bidang_kepakaran.all()])
    get_bidang_kepakaran.short_description = 'Bidang Kepakaran'


admin.site.register(BidangKepakaran, BidangKepakaranAdmin)
admin.site.register(Pakar, PakarAdmin)
admin.site.register(ProgramStudi)

admin.site.register(User)
# class PostNewsAdmin Content
class PostNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(PostNews, PostNewsAdmin)
admin.site.register(Category)
PostNews._meta.verbose_name_plural = "Post News"


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'author__username')
    prepopulated_fields = {'slug': ('title',)}

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        HTMLField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

admin.site.register(Page , PageAdmin)
