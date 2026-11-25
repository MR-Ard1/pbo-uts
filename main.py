# import class
from user import User
from user_Admin import User_Admin
from user_Nasabah import User_Nasabah
from user_NasabahPrioritas import User_NasabahPrioritas
from data_dummy import buat_data

# import Library
from getpass import getpass
# ambil data dummy
admin, nasabah, semua_rekening = buat_data()
semua_user = admin + nasabah # penggabungan data user

if __name__ == "__main__":
    
    def menu_utama():
        print("Selamat datang")
    def menu_admin():
        print("halo admin")
    
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
        print("Selamat datang di Sistem Bank Mini",
              "\n Silahkan Login Terlebih dulu")
        email = input(f"Masukan Email Anda: ")
        pw = getpass("Masukan Password Anda: ")
        
        cek = cek_data_login(email,pw)
        if cek is not None:
            if isinstance(cek, User_Admin):
                menu_admin()
            elif isinstance(cek, User_Nasabah) or isinstance(cek, User_NasabahPrioritas):
                menu_utama()
        else:
            print("Mohon Maaf Login Gagal")
        
    index()  
    
    # for u in semua_user:
    #     print(u.get_id_user(), "|", u.get_nama(), "|", u.get_email(), "|", u.get_pw())         