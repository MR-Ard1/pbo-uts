from rekening import Rekening


class Rekening_Giro(Rekening):
    def __init__(self, no_rek, saldo, biaya_admin, batas_pengambilan,
                 nomor_cek, status="aktif"):
        super().__init__("BCA", no_rek, saldo=saldo, status=status)
        self.__biaya_admin = biaya_admin
        self.__batas_pengambilan = batas_pengambilan
        self.__nomor_cek = nomor_cek

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