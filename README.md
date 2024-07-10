# Kepakaran Web Application

Welcome to the Kepakaran Web Application! This README will guide you through the models used in the application and their functionalities.

![Kepakaran](/screenshot/pakar.bisdigunm.com_.png)

## Models

### 1. User Model
The `User` model extends Django's `AbstractUser` and includes additional fields:
- `is_admin`: Boolean field indicating if the user is an admin.
- `is_staff`: Boolean field indicating if the user is staff.
- `is_dosen`: Boolean field indicating if the user is a faculty member.
- `is_user`: Boolean field indicating if the user is a regular user.
- `phone_number`: Optional phone number field.
- `address`: Optional address field.
- `birth_date`: Optional birth date field.
- `bio`: Optional biography field.
- `image`: Profile image field with a default image.
- `scopus_id`, `sinta`, `google_scholar`, `linkedin`: Optional fields for academic and professional identifiers.

![](/screenshot/pakar.bisdigunm.com_pakar_alamyin_.png)


### 3. Category Model
The `Category` model categorizes content.
- `name`: Name of the category.
- `slug`: Unique slug for the category.

A pre-save signal ensures the `slug` is created from the `name` if not provided.

![](/screenshot/pakar.bisdigunm.com_adminku_accounts_bidangkepakaran_.png)

### 5. ProgramStudi Model
The `ProgramStudi` model represents study programs.
- `nama_program`: Name of the study program.
- `slug`: Unique slug for the study program.

The `get_users` method returns all users associated with the study program.

![](/screenshot/pakar.bisdigunm.com_adminku_accounts_programstudi_.png)

### 6. BidangKepakaran Model
The `BidangKepakaran` model represents fields of expertise.
- `nama_bidang`: Name of the field of expertise.
- `slug`: Unique slug for the field of expertise.

The `get_users` method returns all users associated with the field of expertise.
[](/screenshot/pakar.bisdigunm.com_adminku_accounts_bidangkepakaran_.png)


### 7. Pakar Model
The `Pakar` model represents experts and links them to users.
- `user`: One-to-one field to the `User` model.
- `bidang_kepakaran`: Many-to-many field to the `BidangKepakaran` model.
- `program_studi`: Foreign key to the `ProgramStudi` model.
- `tags`: Tags managed by `TaggableManager`.

### 8. Pendidikan Model
The `Pendidikan` model represents education details of experts.
- `pakar`: Foreign key to the `Pakar` model.
- `pendidikan`: Name of the education.
- `tahun`: Year of completion.
- `program_studi`: Name of the study program.


### 9. Penelitian Model
The `Penelitian` model represents research conducted by experts.
- `pakar`: Foreign key to the `Pakar` model.
- `judul_penelitian`: Title of the research.
- `tahun_penelitian`: Year of the research.
- `link_penelitian`: Optional link to the research.
- `tim_penelitian`: Optional team members.
- `category_penelitian`: Category of the research (Nasional/Internasional).

### 10. InTheNews Model
The `InTheNews` model represents news articles featuring the experts.
- `pakar`: Foreign key to the `Pakar` model.
- `judul_news`: Title of the news article.
- `tanggal_terbit`: Publication date.
- `link_news`: Link to the news article.
- `media`: Media source.
- `picture`: Optional picture associated with the news article.

### 11. Pengabdian Model
The `Pengabdian` model represents community service activities by experts.
- `pakar`: Foreign key to the `Pakar` model.
- `judul_pengabdian`: Title of the community service activity.
- `tahun_pengabdian`: Year of the activity.
- `link_pengabdian`: Optional link to the activity.
- `tim_pengabdian`: Optional team members.

### 12. Book Model
The `Book` model represents books authored by the experts.
- `pakar`: Foreign key to the `Pakar` model.
- `judul_book`: Title of the book.
- `tahun_book`: Year of publication.
- `link_book`: Optional link to the book.
- `penerbit`: Publisher of the book.
- `cover_book`: Optional cover image of the book.

### 13. Organisasi Model
The `Organisasi` model represents organizational memberships or positions held by experts.
- `pakar`: Foreign key to the `Pakar` model.
- `nama_organisasi`: Name of the organization.
- `tahun_organisasi`: Year of the membership or position.
- `jabatan_organisasi`: Position held in the organization.


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