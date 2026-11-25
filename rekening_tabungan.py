from rekening import Rekening


class Rekening_Tabungan(Rekening):
    def __init__(self, no_rek, saldo, bunga, saldo_minimum, tgl_buka,
                 status="aktif"):
        super().__init__("BSA", no_rek, saldo=saldo, status=status)
        self.__bunga = bunga                    # per tahunnya
        self.__saldo_minimum = saldo_minimum    # endapan dana
        self.__tgl_buka = tgl_buka

    # getter
    def get_bunga(self):
        return self.__bunga

    def get_saldo_minimum(self):
        return self.__saldo_minimum

    def get_tgl_buka(self):
        return self.__tgl_buka

    # fungsi lainnya
    def hitung_bunga(self):
        return self.get_saldo() * self.__bunga / 12 # hitung bunga untuk tiap bulan

    def kurang_saldo(self, nominal):
        if self.get_status() != "aktif" or nominal <= 0:
            return False
        if self.get_saldo() - nominal < self.__saldo_minimum:
            return False
        self._ubah_saldo(-nominal)
        return True
   
   
# uji
    def lihat(self):
        super().lihat()
        print(f"Bunga : {self.get_bunga()}")
        print(f"Tangal : {self.get_tgl_buka()}")