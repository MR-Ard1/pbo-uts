class Transaksi:
    __count = 0
    def __init__(self, rekening, id_pengguna, jenis_transaksi, nominal,
                 biaya_admin, tgl_transaksi):
        Transaksi.__count += 1
        self.__id_transaksi = "TRX-" + str(Transaksi.__count).zfill(5)
        self.__rekening = rekening             
        self.__id_pengguna = id_pengguna
        self.__jenis_transaksi = jenis_transaksi
        self.__nominal = nominal
        self.__biaya_admin = biaya_admin
        self.__tgl_transaksi = tgl_transaksi

    # getter
    def get_id_transaksi(self):
        return self.__id_transaksi

    def get_rekening(self):
        return self.__rekening

    def get_id_pengguna(self):
        return self.__id_pengguna

    def get_jenis_transaksi(self):
        return self.__jenis_transaksi

    def get_nominal(self):
        return self.__nominal

    def get_biaya_admin(self):
        return self.__biaya_admin

    def get_tgl_transaksi(self):
        return self.__tgl_transaksi

    # fungsi lainnya
    def cetak_bukti(self):
        print("===== BUKTI TRANSAKSI =====")
        print(f"ID        : {self.__id_transaksi}")
        print(f"Tanggal   : {self.__tgl_transaksi}")
        print(f"Rekening  : {self.__rekening.get_no_rek()}")
        print(f"Jenis     : {self.__jenis_transaksi}")
        print(f"Nominal   : {self.__nominal}")
        print(f"Biaya     : {self.__biaya_admin}")
        print(f"Total     : {self.__nominal + self.__biaya_admin}")

    def cari_riwayat(self, daftar_transaksi):
        no_rek = self.__rekening.get_no_rek()
        return [t for t in daftar_transaksi
                if t.get_rekening().get_no_rek() == no_rek]