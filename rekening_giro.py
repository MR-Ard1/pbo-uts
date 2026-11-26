from rekening import Rekening


class Rekening_Giro(Rekening):
    BIAYA_ADMIN_DEFAULT = 10_000
    BATAS_DEFAULT = 200_000
    __count_cek = 0  
    def __init__(self, no_rek, saldo,
                 biaya_admin=BIAYA_ADMIN_DEFAULT, batas_pengambilan=BATAS_DEFAULT,
                 status="aktif"):
        super().__init__("BCA", no_rek, saldo=saldo, status=status)
        Rekening_Giro.__count_cek += 1          
        self.__biaya_admin = biaya_admin
        self.__batas_pengambilan = batas_pengambilan
        self.__nomor_cek = "CEK-" + str(Rekening_Giro.__count_cek).zfill(5)

    # getter
    def get_biaya_admin(self):
        return self.__biaya_admin

    def get_batas_pengambilan(self):
        return self.__batas_pengambilan

    def get_nomor_cek(self):
        return self.__nomor_cek

    # fungsi lainnya
    def potong_biaya_bulanan(self):
        self._ubah_saldo(-self.__biaya_admin)

    def kurang_saldo(self, nominal):
        if self.get_status() != "aktif" or nominal <= 0:
            return False
        if self.get_saldo() - nominal < -self.__batas_pengambilan:
            return False
        self._ubah_saldo(-nominal)
        return True



# uji
    def lihat(self):
        super().lihat()
        print(f"No Cek : {self.get_nomor_cek()}")
        print(f"Batas : {self.get_batas_pengambilan()}")