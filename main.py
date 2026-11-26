# import class
from user import User
from user_Admin import User_Admin
from user_Nasabah import User_Nasabah
from user_NasabahPrioritas import User_NasabahPrioritas
from data_dummy import buat_data
from rekening_tabungan import Rekening_Tabungan
from rekening_giro import Rekening_Giro

# import Library
from getpass import getpass
from datetime import date
import random
import math

# ambil data dummy
admin, nasabah, semua_rekening = buat_data()
semua_user = admin + nasabah # penggabungan data user

if __name__ == "__main__":
    
    def baca_nominal(teks):
        nilai = float(input(teks))          # ValueError kalau huruf
        if not math.isfinite(nilai):
            raise ValueError("Nominal tidak valid")
        return nilai
    
    # no rek otomatis
    def buat_no_rek(awalan):
        while True:
            no_rek = awalan + str(random.randint(0, 10**8 - 1)).zfill(8)
            if not any(r.get_no_rek() == no_rek for r in semua_rekening):
                return no_rek
    
    # fungsi daftar menu Nasabah
    def menu_top_up(user):
        try:
            no_rek = input("No. rekening: ")
            nominal = baca_nominal("Nominal: ")
            user.tambah_saldo(no_rek, nominal)    # methode ada di class user nasabah
            print("Top up berhasil")
        except ValueError as e:
            print("Gagal:", e)
    
    def menu_cari_rekening(user):
        no_rek = input("No. rekening: ").strip()
        r = user.cari_rekening(no_rek)       # Methode di class User nasabah
        if r is None:
            print("Rekening tidak ditemukan")
        else:
            r.lihat()
            
    def menu_buka_rekening(user):
        jenis = input("Jenis (1. Tabungan, 2. Giro): ").strip() # pilih mau buka rekening apa
        if jenis not in ("1", "2"):
            print("Jenis tidak valid")
            return
        try:
            saldo = baca_nominal("Setoran awal: ") # minta setoran awal
        except ValueError:
            print("Input angka tidak valid, rekening batal dibuat")
            return
        no_rek = buat_no_rek("1" if jenis == "1" else "2")
        try:
            if jenis == "1":
                rek = Rekening_Tabungan(no_rek, saldo, date.today())
            else:
                rek = Rekening_Giro(no_rek, saldo)
        except ValueError as e:
            print("Gagal:", e)
            return
        user.buka_rekening(rek)
        semua_rekening.append(rek)
        print("Rekening berhasil dibuka")
        print("ID      :", rek.get_id())
        print("No. Rek :", no_rek)
        
    def menu_daftar_rekening(user):
        daftar = user.get_daftar_rekening()
        if not daftar:                       
            print("Belum punya rekening")
            return
        for r in daftar:
            print("---")
            r.lihat()
            
    def menu_top_up(user):
        try:
            no_rek = input("No. rekening: ").strip()
            nominal = baca_nominal("Nominal top up: ")
            user.tambah_saldo(no_rek, nominal)
            print("Top up berhasil")
        except ValueError as e:
            print("Gagal:", e)
            
    def menu_transfer(user):
        try:
            asal = input("No. rekening asal (milik Anda): ").strip()
            tujuan_no = input("No. rekening tujuan: ").strip()
            if asal == tujuan_no:
                print("Rekening asal dan tujuan tidak boleh sama")
                return
            tujuan = None
            for r in semua_rekening:
                if r.get_no_rek() == tujuan_no:
                    tujuan = r
                    break
            if tujuan is None:
                print("Rekening tujuan tidak ditemukan")
                return
            nominal = baca_nominal("Nominal transfer: ")
            if user.transfer_saldo(asal, tujuan, nominal):
                print("Transfer berhasil")
        except ValueError as e:
            print("Gagal:", e)
    
    def menu_ubah_data(user):
        print("Kosongkan jika tidak ingin diubah")
        nama = input("Nama baru: ").strip() or None
        no_hp = input("No. HP baru: ").strip() or None
        email = input("Email baru: ").strip() or None
        nama_ibu = input("Nama ibu baru: ").strip() or None
        tgl_teks = input("Tgl lahir baru (YYYY-MM-DD): ").strip()
        try:
            tgl = date.fromisoformat(tgl_teks) if tgl_teks else None
            user.ubah_data(nama=nama, no_hp=no_hp, email=email,
                        tgl_lahir=tgl, nama_ibu=nama_ibu)
            print("Data berhasil diperbarui")
        except ValueError as e:
            print("Gagal:", e)
    
    def menu_cek_status(user):
        no_rek = input("No. rekening: ").strip()
        r = user.cari_rekening(no_rek)
        if r is None:
            print("Rekening tidak ditemukan")
        else:
            print(f"Status rekening {no_rek}: {r.get_status()}")
    
    # program menu
    def menu_utama(user):
        list_menu = [("lihat profil",lambda user:user.lihat_profil() ), # methode ada di class user
                    ("Lihat daftar rekening", menu_daftar_rekening),
                    ("Cari rekening",         menu_cari_rekening),
                    ("Buka rekening",         menu_buka_rekening),
                    ("Top up saldo",          menu_top_up),
                    ("Transfer",              menu_transfer),
                    ("Perbarui info",         menu_ubah_data),
                    ("Riwayat transfer",      lambda u: u.cek_riwayat_transaksi()),
                    ("Cek status rekening",   menu_cek_status), # methode ada di class user nasabah
                     ]
        no_exit = len(list_menu)+1
        while True:
            print(f"\n=== MENU NASABAH ({user.get_nama()}) ===")
            for i, (nama_menu, _) in enumerate(list_menu, start=1):
                print(f"{i}. {nama_menu}")
            print(f"{no_exit}. Keluar")

            try:
                pilihan = int(input("Pilih menu (angka): "))
            except ValueError:
                print("Pilihan harus berupa angka!")
                continue

            if pilihan == no_exit:
                print("Sampai jumpa!")
                break
            if pilihan < 1 or pilihan > len(list_menu):
                print(f"Menu {pilihan} tidak tersedia")
                continue

            list_menu[pilihan - 1][1](user) 
                
    # fungsi daftar menu Admin
    def cari_rekening_global(no_rek):
        for r in semua_rekening:
            if r.get_no_rek() == no_rek:
                return r
        return None

    def menu_admin_cari(user):
        kata = input("Cari (nama / id nasabah / no. rekening): ").strip().lower()
        if not kata:
            print("Kata kunci kosong")
            return
        ditemukan = False
        for n in nasabah:
            if kata in n.get_nama().lower() or kata == n.get_id_user().lower():
                ditemukan = True
                print("=" * 40)
                print(f"[NASABAH] {n.get_id_user()} | {n.get_nama()} | {n.get_email()}")
                print(f"Jumlah rekening: {len(n.get_daftar_rekening())}")
        r = cari_rekening_global(kata)
        if r is not None:
            ditemukan = True
            print("=" * 40)
            print("[REKENING]")
            r.lihat()
        if not ditemukan:
            print("Data tidak ditemukan")

    def menu_admin_tutup(user):
        no_rek = input("No. rekening yang akan ditutup: ").strip()
        r = cari_rekening_global(no_rek)
        if r is None:
            print("Rekening tidak ditemukan")
            return
        yakin = input(f"Yakin tutup rekening {no_rek}? (y/n): ").strip().lower()
        if yakin == "y":
            user.tutup_rekening(r)    # mehode di class user admin
        else:
            print("Dibatalkan")

    def menu_admin_status(user):
        no_rek = input("No. rekening: ").strip()
        r = cari_rekening_global(no_rek)
        if r is None:
            print("Rekening tidak ditemukan")
        else:
            print(f"Status rekening {no_rek}: {r.get_status()}")

    def menu_admin(user):
        menu = [
            ("Lihat profil",              lambda u: u.lihat_profil()),
            ("Lihat info user & rekening", lambda u: u.lihat_semua_info(nasabah)),
            ("Cari nasabah / rekening",   menu_admin_cari),
            ("Tutup rekening",            menu_admin_tutup),
            ("Cek status rekening",       menu_admin_status),
            ("Cetak laporan",             lambda u: u.cetak_laporan(nasabah)),
        ]
        nomor_keluar = len(menu) + 1
        while True:
            print(f"\n=== MENU ADMIN ({user.get_nama()}) ===")
            for i, (nama_menu, _) in enumerate(menu, start=1):
                print(f"{i}. {nama_menu}")
            print(f"{nomor_keluar}. Keluar")

            try:
                pilihan = int(input("Pilih menu (angka): "))
            except ValueError:
                print("Pilihan harus berupa angka!")
                continue

            if pilihan == nomor_keluar:
                print("Sampai jumpa!")
                break
            if pilihan < 1 or pilihan > len(menu):
                print(f"Menu {pilihan} tidak tersedia")
                continue

            menu[pilihan - 1][1](user)
        
    # prefix  user : CC = customer client, HNW = High Net Worth, ADM = Admin
    # prefix Rekening : BSA = Bank Saving Accounts, BCA = Bank Current Account
    # prefix Lainnya : TRX = Transaksi
    
    def cek_data_login(email,pw):
        global semua_user
        for user in semua_user: # Prosespengecekan dan pencarian data login dari semua pengguna
            if user.get_email() == email:
                if user.login(email,pw):
                    return user # mengembalikan data yang sesuai
                return None
        print(f"{email} Tidak Terdaftar")
        return None
        
    def index():
        print("\nSelamat datang di Sistem Bank Mini")
        print("Silakan login terlebih dahulu")

        for _ in range(3): # maksimal 3 kali percobaan
            email = input("Masukkan Email Anda: ").strip()
            pw = getpass("Masukkan Password Anda: ")
            user = cek_data_login(email, pw)

            if user is None:
                print("Mohon maaf, login gagal\n")
                continue

            if isinstance(user, User_Admin):
                menu_admin(user)
            elif isinstance(user, User_Nasabah):
                menu_utama(user)
            return
        print("Gagal 3 kali, program ditutup.")
        
    index()  