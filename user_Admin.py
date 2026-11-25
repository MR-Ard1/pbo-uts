from user import User


class User_Admin(User):
    __count = 0   
    def __init__(self, nama, no_hp, email, password, id_pegawai, jabatan, shift_kerja):
        User_Admin.__count += 1
        _newid = "ADM-" + str(User_Admin.__count).zfill(4)
        super().__init__(_newid, nama, no_hp, email, password)
        self.__id_pegawai = id_pegawai
        self.__jabatan = jabatan
        self.__shift_kerja = shift_kerja
        
# getter
    def get_id_pegawai(self):
        return self.__id_pegawai

    def get_jabatan(self):
        return self.__jabatan

    def get_shift_kerja(self):
        return self.__shift_kerja
    
# fungsi lainnya
    def tutup_rekening(self, rekening):
        if rekening.get_status() == "ditutup":
            print("Rekening", rekening.get_no_rek(), "sudah ditutup.")
            return False
        rekening.tutup()
        print("Rekening", rekening.get_no_rek(), "ditutup oleh", self.get_nama())
        return True
    
    def lihat_semua_info(self, daftar_nasabah):
        # menampilkan semua nasabah beserta rekeningnya
        for n in daftar_nasabah:
            print("=" * 40)
            print(f"ID    : {n.get_id_user()}")
            print(f"Nama  : {n.get_nama()}")
            print(f"Email : {n.get_email()}")
            rekening = n.get_daftar_rekening()
            if len(rekening) == 0:
                print("  (belum punya rekening)")
            for r in rekening:
                print("  ---")
                r.lihat()  
                
    def cetak_laporan(self, daftar_nasabah):
        # ringkasan seluruh bank
        jumlah_rek = 0
        total_saldo = 0
        aktif = 0
        jumlah_transaksi = 0
        for n in daftar_nasabah:
            jumlah_transaksi += len(n.get_riwayat_transaksi())
            for r in n.get_daftar_rekening():
                jumlah_rek += 1
                total_saldo += r.get_saldo()
                if r.get_status() == "aktif":
                    aktif += 1

        print("===== LAPORAN BANK MINI =====")
        print(f"Dicetak oleh      : {self.get_nama()} ({self.__id_pegawai})")
        print(f"Jumlah nasabah    : {len(daftar_nasabah)}")
        print(f"Jumlah rekening   : {jumlah_rek} (aktif: {aktif}, ditutup: {jumlah_rek - aktif})")
        print(f"Total saldo       : {total_saldo}")
        print(f"Jumlah transaksi  : {jumlah_transaksi}")