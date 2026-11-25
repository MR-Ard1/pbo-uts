class Rekening:
    __count = 0
    def __init__(self,prefix, no_rek, saldo, status="aktif"):
        Rekening.__count += 1
        self.__id = prefix + "-"+ str(Rekening.__count).zfill(5)
        self.__no_rek = no_rek
        self.__saldo = saldo
        self.__status = status

    # getter
    def get_id(self):
        return self.__id

    def get_no_rek(self):
        return self.__no_rek

    def get_status(self):
        return self.__status

    def get_saldo(self):
        return self.__saldo

    # setter
    def _set_saldo(self, selisih):
        self.__saldo += selisih
        
    # fungsi lainnya
    def _ubah_saldo(self, selisih):
        self.__saldo += selisih

    def tambah_saldo(self, nominal):
        if self.__status != "aktif":
            raise ValueError("Rekening tidak aktif".title())
        if nominal <= 0:
            raise ValueError("Nominal harus lebih dari 0".title())
        self.__saldo += nominal

    def kurang_saldo(self, nominal):
        if self.__status != "aktif" or nominal > self.__saldo:
            return False
        self.__saldo -= nominal
        return True

    def tutup(self): # admin
        self.__status = "ditutup"
        
    # uji
    def lihat(self):
        print(f"ID : {self.get_id()}")
        print(f"No. Rek : {self.get_no_rek()}")
        print(f"Status : {self.get_status()}")
        print(f"Saldo : {self.get_saldo()}")