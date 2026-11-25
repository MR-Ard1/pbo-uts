from user import User
from transaksi import Transaksi
from datetime import date

class User_Nasabah(User):
    admintf = 5000
    __count = {}                      
    def __init__(self, nama, no_hp, email, password, nama_ibu, tgl_lahir,
                 prefix="CC"):         # CC = Common Customer
        User_Nasabah.__count[prefix] = User_Nasabah.__count.get(prefix, 0) + 1
        _newid = prefix + "-" + str(User_Nasabah.__count[prefix]).zfill(4)
        super().__init__(_newid, nama, no_hp, email, password)
        self.__nama_ibu = nama_ibu.upper()
        self.__daftar_rekening = []
        self.__riwayat_transaksi = []
        self.__tgl_lahir = tgl_lahir
        
        
# getter
    def get_nama_ibu(self):
        return self.__nama_ibu
    def get_tgl_lahir(self):
        return self.__tgl_lahir
    def get_daftar_rekening(self):
        return self.__daftar_rekening

    def get_riwayat_transaksi(self):
        return self.__riwayat_transaksi
    
# fungsi lainnya
    hitung_admin = lambda self, admintf: admintf  # fungsi hitung biaya admin
    
    def ubah_data(self, nama = None, no_hp = None, email = None, tgl_lahir = None, nama_ibu = None):
        # proses penyimpanan
        if nama is not None:
            self.set_nama(nama)  
        if nama_ibu is not None:
            self.__nama_ibu = nama_ibu.upper()
        if no_hp is not None:
            self.set_no_hp(no_hp) 
        if email is not None:
            self.set_email(email)
        if tgl_lahir is not None:
            self.__tgl_lahir = tgl_lahir
    
    def buka_rekening(self,rek):
        self.__daftar_rekening.append(rek)
        
    def cari_rekening(self, no_rek):
        for i in self.__daftar_rekening: #cari rekening yg di miliki
            if i.get_no_rek() == no_rek:
                return i
        return None
    
    def tambah_saldo(self, no_rek,nominal):
        rekening = self.cari_rekening(no_rek)
        if rekening is None:
            raise ValueError("Rekening tidak ditemukan")

        rekening.tambah_saldo(nominal) # penambahan saldo
        
        # proses membuat history
        transaksi = Transaksi(rekening, self.get_id_user(), "top up", nominal, 0, date.today())
        self.__riwayat_transaksi.append(transaksi)
        return True
    
    def transfer_saldo(self,no_rek,tujuan,nominal):
        if nominal <= 0:
            raise ValueError("Nominal transfer harus lebih dari 0")

        asal = self.cari_rekening(no_rek)
        if asal is None:
            raise ValueError("Rekening asal tidak ditemukan")

        if tujuan.get_status() != "aktif":
            print("Rekening tujuan tidak aktif.")
            return False
        biaya = self.hitung_admin(self.admintf)
        # print(f"biaya : {biaya} ")    
        if not asal.kurang_saldo(nominal + biaya):
            print("Saldo tidak cukup.")
            return False

        tujuan.tambah_saldo(nominal) 
        transaksi = Transaksi(asal, self.get_id_user(), "transfer",
                              nominal, biaya, date.today())
        self.__riwayat_transaksi.append(transaksi)
        return True

    def cek_riwayat_transaksi(self):
        hasil = [t for t in self.__riwayat_transaksi
                 if t.get_jenis_transaksi() == "transfer"]
        if len(hasil) == 0:
            print("Belum ada riwayat transfer.")
        for t in hasil:
            t.cetak_bukti()
        return hasil
    
    
    