from user_Nasabah import User_Nasabah

class User_NasabahPrioritas(User_Nasabah):
    __TabelPrioritas ={
        "VIP": {"diskon": 0.10, "limit":5*10**7, "bunga":0.02}, # 50 jt
        "VVIP": {"diskon": 0.20, "limit":1*10**8, "bunga":0.04}, # 100jt
        "LUXURYVVIP": {"diskon": 0.40, "limit":5*10**8, "bunga":0.10} # 500jt
    }
    def __init__(self, nama, no_hp, email, password, nama_ibu, tgl_lahir,
                 lvl_prioritas):
        super().__init__(nama, no_hp, email, password, nama_ibu, tgl_lahir,
                         prefix="HNW")
        self.__lvl_prioritas = None
        self.__diskon_admin = 0
        self.__limit_transaksi = 0
        self.__bunga = 0
        self.set_lvl(lvl_prioritas)


# getter
    def get_lvl_prioritas(self):
        return self.__lvl_prioritas
    
    def get_diskon_admin(self):
        return self.__diskon_admin
    
    def get_limit_transaksi(self):
        return self.__limit_transaksi
    
    def get_bunga(self):
        return self.__bunga
    
# setter
    def set_lvl(self,lvl):
        key = lvl.strip().upper()
        if key not in self.__TabelPrioritas:
            raise ValueError(" Layanan tidak tersedia")
        # simpan data
        self.__lvl_prioritas = key
        self.__diskon_admin = self.__TabelPrioritas[key]["diskon"]
        self.__limit_transaksi = self.__TabelPrioritas[key]["limit"]
        self.__bunga = self.__TabelPrioritas[key]["bunga"]

# fungsi lainnya
    def hitung_admin(self, admintf):
        return admintf * (1 - self.__diskon_admin)
    
    def transfer_saldo(self,no_rek,tujuan,nominal):
        # validasi limit
        if nominal > self.__limit_transaksi:
            print("Melebihi limit transfer level", self.__lvl_prioritas)
            return False
        return super().transfer_saldo(no_rek, tujuan, nominal)