from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Penelitian, Book, InTheNews, Organisasi, Pendidikan, Pengabdian, BidangKepakaran, Pakar
from tinymce.widgets import TinyMCE
from taggit.forms import TagWidget



class MinatPenelitianForm(forms.ModelForm):
    class Meta:
        model = Pakar
        fields = ['tags']
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Masukkan minat penelitian, pisahkan dengan koma'}),
        }


class PakarForm(forms.ModelForm):
    class Meta:
        model = Pakar
        fields = ['bidang_kepakaran', 'program_studi']
        widgets = {
            'bidang_kepakaran': forms.CheckboxSelectMultiple,
        }



class PengabdianForm(forms.ModelForm):
    class Meta:
        model = Pengabdian
        fields = ['judul_pengabdian', 'tahun_pengabdian', 'link_pengabdian', 'tim_pengabdian']

class PendidikanForm(forms.ModelForm):
    class Meta:
        model = Pendidikan
        fields = ['pendidikan', 'tahun', 'program_studi']

class OrganisasiForm(forms.ModelForm):
    class Meta:
        model= Organisasi
        fields = ['nama_organisasi', 'tahun_organisasi', 'jabatan_organisasi']


class NewsForm(forms.ModelForm):

    tanggal_terbit = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = InTheNews
        fields = ['judul_news', 'tanggal_terbit', 'link_news', 'media']

class PenelitianForm(forms.ModelForm):
    class Meta:
        model = Penelitian
        fields = ['judul_penelitian', 'tahun_penelitian', 'link_penelitian', 'tim_penelitian', 'category_penelitian']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['judul_book', 'tahun_book', 'link_book', 'penerbit', 'cover_book']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2', 'is_user')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = self.cleaned_data["phone_number"]
        user.is_pelanggan = self.cleaned_data["is_user"]
        if commit:
            user.save()
        return user
    
    def clean_is_pelanggan(self):
        is_pelanggan = self.cleaned_data.get("is_user")
        if not is_pelanggan:
            raise forms.ValidationError("You must agree to our Terms...")
        return is_pelanggan

    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email has been registered...")
        return email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'bio', 'image', 'scopus_id', 'sinta', 'google_scholar', 'linkedin']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Tambahkan validasi email di sini jika diperlukan
        return email



class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()


class PasswordResetConfirmForm(forms.Form):
    verification_code = forms.CharField(max_length=6)
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    


# class PageForm(forms.ModelForm):

#     content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    
#     class Meta:
#         model = Page
#         fields = '__all__'

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)