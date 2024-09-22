# Indovina - A Simple E-Commerce System

# Overview
Indovina is a simple e-commerce system that allows users to browse, add items to their cart, and make payments. 
The system supports two types of users: buyers and sellers. 
Buyers can purchase food, drinks, snacks, and medicines, while sellers can manage the inventory of these items.

# Features
User Roles : Supports both buyer and seller.
※ For Seller, need to input a password

Product Categories : Users can navigate through various sections including Foods, Drinks, Snacks, and Meds.

Buyer Features :
Display Product : Buyer can browse items that displayed by seller on each catgories.
Shopping Cart : Buyers have their own cart.
Add Item to Cart : Buyers can add item they want to buy to the cart.
Discard Item from Cart : Buyers can discard item they have added from cart.
Payment : Buyer can pay for the item in the cart (checkout)
※ Once buyer in payment feature, buyer can’t go back (must pay first)
Exit : Buyer can go back to user roles menu

Seller Features : 
Display Product : Seller can browse items that displayed on each catgories
Add items to various section : Seller can add new items and add stock to the choosen section.
Erase items on each section : Seller can erase items on each section. 
 ※ Erased items, not reducing stock
Exit : Seller can go back to user roles menu

# User Guide
Choose Role: Upon startup, the user will be prompted to select either "Buyer" or "Seller".

Buyer Functionality:
Browse Sections: Buyers can choose from different sections: Foods, Drinks, Snacks, and Meds.
Add to Cart: Buyers can select items to add to their shopping cart.
Discard Items: Buyers can remove items from their cart if needed.
Payment: Buyers can finalize their purchases and receive a change if they pay more than the total.

Seller Functionality:
Display Items: Sellers can view the items available in each section.
Add Items: Sellers can add new items to the inventory or update the stock of existing items.
Remove Items: Sellers can remove items from the inventory.

# Inventory Structure
Each product category has the following attributes :
Foods : 
Name, Stock, Spice Level (Spicy/Mild), Portion Size(Big/Medium/Small), Price
Drinks : 
Name, Stock, Category (Alcohol/Non-alcohol), Portion Size(Big/Medium/Small), Price
Snacks : 
Name, Stock, Portion Size(Big/Medium/Small), Price
Meds : 
Name, Stock, Indication, Price

# Code Explanation
The program uses the tabulate library to display data in a table format for better readability.
Various functions handle different functionalities, including displaying items, adding to the cart, discarding items, and processing payments.
The inventory is managed through lists, and indexing is implemented to ensure the correct items are referenced.

# Requirements
Python 3.x
tabulate library (Install using pip install tabulate)

##### TRANSLATION #####

# Indovina - Sistem E-Commerce Sederhana

# Gambaran Umum
Indovina adalah sistem e-commerce sederhana yang memungkinkan pengguna untuk melihat produk, menambahkan item ke keranjang belanja, dan melakukan pembayaran. 
Sistem ini mendukung dua jenis pengguna: pembeli dan penjual. 
Pembeli dapat membeli makanan, minuman, camilan, dan obat-obatan, sementara penjual dapat mengelola persediaan item-item tersebut.

# Fitur-Fitur
Peran Pengguna : Mendukung pembeli dan penjual.
※ Untuk penjual, diperlukan kata sandi untuk login.
Kategori Produk : Pengguna dapat menavigasi berbagai bagian, termasuk Makanan, Minuman, Camilan, dan Obat-Obatan.
Fitur Pembeli :
Tampilkan Produk : Pembeli dapat melihat item yang ditampilkan oleh penjual di setiap kategori.
Keranjang Belanja : Pembeli memiliki keranjang belanja sendiri.
Tambahkan Item ke Keranjang : Pembeli dapat menambahkan item yang ingin dibeli ke dalam keranjang.
Buang Item dari Keranjang : Pembeli dapat membuang item yang telah ditambahkan ke keranjang.
Pembayaran : Pembeli dapat membayar item yang ada di keranjang (checkout).
※ Setelah pembeli masuk ke fitur pembayaran, mereka tidak dapat kembali (harus membayar terlebih dahulu).
Keluar : Pembeli dapat kembali ke menu peran pengguna.
Fitur Penjual :
Tampilkan Produk : Penjual dapat melihat item yang ditampilkan di setiap kategori.
Tambahkan Item ke Berbagai Kategori : Penjual dapat menambahkan item baru dan menambah stok ke kategori yang dipilih.
Hapus Item dari Setiap Kategori : Penjual dapat menghapus item dari setiap kategori.
※ Item yang dihapus, tidak mengurangi stok.
Keluar : Penjual dapat kembali ke menu peran pengguna.

# Panduan Pengguna
Pilih Peran : Setelah program dijalankan, pengguna akan diminta untuk memilih sebagai "Pembeli" atau "Penjual".
Fungsi Pembeli:
Telusuri Kategori : Pembeli dapat memilih dari berbagai kategori: Makanan, Minuman, Camilan, dan Obat-Obatan.
Tambahkan ke Keranjang : Pembeli dapat memilih item untuk ditambahkan ke keranjang belanja.
Buang Item : Pembeli dapat menghapus item dari keranjang jika diperlukan.
Pembayaran : Pembeli dapat menyelesaikan pembelian dan mendapatkan kembalian jika mereka membayar lebih dari total harga.
Fungsi Penjual:
Tampilkan Item : Penjual dapat melihat item yang tersedia di setiap kategori.
Tambahkan Item : Penjual dapat menambahkan item baru ke inventaris atau memperbarui stok item yang sudah ada.
Hapus Item : Penjual dapat menghapus item dari inventaris.

# Struktur Inventori
Setiap kategori produk memiliki atribut berikut :
Makanan :
Nama, Stok, Tingkat Kepedasan (Pedas/Manis), Ukuran Porsi (Besar/Sedang/Kecil), Harga
Minuman :
Nama, Stok, Kategori (Beralkohol/Tanpa Alkohol), Ukuran Porsi (Besar/Sedang/Kecil), Harga
Camilan :
Nama, Stok, Ukuran Porsi (Besar/Sedang/Kecil), Harga
Obat-Obatan :
Nama, Stok, Indikasi, Harga

# Penjelasan Kode
Program ini menggunakan pustaka tabulate untuk menampilkan data dalam format tabel agar lebih mudah dibaca.
Berbagai fungsi menangani berbagai fungsionalitas, termasuk menampilkan item, menambahkan ke keranjang, membuang item, dan memproses pembayaran.
Inventaris dikelola melalui daftar (list), dan pengindeksan diterapkan untuk memastikan item yang benar dirujuk.

# Persyaratan
Python 3.x
pustaka tabulate (Install dengan pip install tabulate)
