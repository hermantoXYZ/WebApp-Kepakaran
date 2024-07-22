# Kepakaran Web Application

Welcome to the Kepakaran Web Application! This README will guide you through the models used in the application and their functionalities.

![Kepakaran](/screenshot/pakar.bisdigunm.com_.png)

## Models

### 1. User Model
The `User` model extends Django's `AbstractUser` and includes additional fields:
- `is_admin`: 
- `is_staff`: 
- `is_dosen`: 
- `is_user`: 
- `phone_number`: 
- `address`: 
- `birth_date`: 
- `bio`: 
- `image`: 
- `scopus_id`, `sinta`, `google_scholar`, `linkedin`: Optional fields for academic and professional identifiers.

![](/screenshot/pakar.bisdigunm.com_pakar_alamyin_.png)


### 3. Category Model
The `Category` model categorizes content.
- `name`: N
- `slug`: 

A pre-save signal ensures the `slug` is created from the `name` if not provided.

![](/screenshot/pakar.bisdigunm.com_adminku_accounts_bidangkepakaran_.png)

### 5. ProgramStudi Model
The `ProgramStudi` model represents study programs.
- `nama_program`: 
- `slug`: 

The `get_users` method returns all users associated with the study program.

![](/screenshot/pakar.bisdigunm.com_adminku_accounts_programstudi_.png)

### 6. BidangKepakaran Model
The `BidangKepakaran` 
- `nama_bidang`: 
- `slug`: 

The `get_users` method returns all users associated with the field of expertise.
[](/screenshot/pakar.bisdigunm.com_adminku_accounts_bidangkepakaran_.png)


### 7. Pakar Model
The `Pakar` model represents experts and links them to users.
- `user`: O
- `bidang_kepakaran`: 
- `program_studi`:
- `tags`: Tags managed by `TaggableManager`.

![](/screenshot/pakar.bisdigunm.com_search__query=a.png)

### 8. Pendidikan Model
The `Pendidikan` model represents education details of experts.
- `pakar`: 
- `pendidikan`:
- `tahun`: 
- `program_studi`


### 9. Penelitian Model
The `Penelitian` model represents research conducted by experts.
- `pakar`: Foreign key to the `Pakar` model.
- `judul_penelitian`: 
- `tahun_penelitian`: 
- `link_penelitian`: 
- `tim_penelitian`:
- `category_penelitian`: Category of the research (Nasional/Internasional).

![](/screenshot/pakar.bisdigunm.com_dashboard_dosen_list_penelitian.png)

### 10. InTheNews Model
The `InTheNews` model represents news articles featuring the experts.
- `pakar`: 
- `judul_news`: 
- `tanggal_terbit`:
- `link_news`:
- `media`: 
- `picture`: 

![](/screenshot/pakar.bisdigunm.com_dashboard_dosen.png)

### 11. Pengabdian Model
The `Pengabdian` model represents community service activities by experts.
- `pakar`
- `judul_pengabdian`
- `tahun_pengabdian`:
- `link_pengabdian`
- `tim_pengabdian`

### 12. Book Model
The `Book` model represents books authored by the experts.
- `pakar`: 
- `judul_book`
- `tahun_book`
- `link_book`
- `penerbit`:
- `cover_book`

### 13. Organisasi Model
The `Organisasi` model represents organizational memberships or positions held by experts.
- `pakar`
- `nama_organisasi`
- `tahun_organisasi`
- `jabatan_organisasi`


# Dashboard Admin

## 1 Login `Akses to Dashboard`
![](/screenshot/pakar.bisdigunm.com_adminku_login__next=_adminku_.png)
---

## 2 List Model
![](/screenshot/pakar.bisdigunm.com_adminku_.png)
---

## 3 Select bidang kepakaran to change 
![](/screenshot/pakar.bisdigunm.com_adminku_accounts_bidangkepakaran_.png)

## 4 Select pakar to change 
![](/screenshot/pakar.bisdigunm.com_adminku_accounts_pakar_%20(1).png)

## 5 Change pakar 
![](/screenshot/pakar.bisdigunm.com_adminku_accounts_pakar_2_change_.png)

## 6 Change Pendidikan
![](/screenshot/pakar.bisdigunm.com_adminku_accounts_pakar_2_change_%20(1).png)

## 7 Change PENGABDIAN
![](/screenshot/pakar.bisdigunm.com_adminku_accounts_pakar_2_change_%20(2).png)

## 8 Change ORGANISASI
![](/screenshot/pakar.bisdigunm.com_adminku_accounts_pakar_2_change_%20(3).png)


## 9 Change Books 
![](/screenshot/pakar.bisdigunm.com_adminku_accounts_pakar_2_change_%20(4).png)

## 10 Change News 
![](/screenshot/pakar.bisdigunm.com_adminku_accounts_pakar_2_change_%20(5).png)


This README provides an overview of the models used in the Kepakaran Web Application. For further details on implementation and usage, please refer to the specific model definitions and their methods.


#UPDATE