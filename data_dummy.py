from datetime import date
from user_Nasabah import User_Nasabah
from user_NasabahPrioritas import User_NasabahPrioritas   # sesuaikan nama file
from user_Admin import User_Admin                         # sesuaikan nama file
from rekening_tabungan import Rekening_Tabungan
from rekening_giro import Rekening_Giro


def _buat_admin():
    # (nama, no_hp, email, password, id_pegawai, jabatan, shift)
    data = [
        ("ridwan", "081200000101", "ridwan@bank.com", "admin101", "P-001", "Kepala Operasional", "Pagi"),
        ("maya",   "081200000102", "maya@bank.com",   "admin102", "P-002", "Staf Layanan",       "Siang"),
        ("bagas",  "081200000103", "bagas@bank.com",  "admin103", "P-003", "Staf Laporan",       "Malam"),
    ]
    return [User_Admin(*d) for d in data]

def _buat_nasabah():
    # nasabah biasa: (nama, no_hp, email, password, nama_ibu, tgl_lahir)
    budi = User_Nasabah("budi santoso", "081211110001", "budi@mail.com",
                        "budi123", "sri wahyuni", date(2005, 3, 14))
    andi = User_Nasabah("andi pratama", "081211110003", "andi@mail.com",
                        "andi123", "lina marlina", date(2003, 9, 2))
    # prioritas: tambah level di akhir
    siti = User_NasabahPrioritas("siti aminah", "081211110002", "siti@mail.com",
                                 "siti123", "ratna dewi", date(2004, 7, 21), "vvip")
    dewi = User_NasabahPrioritas("dewi lestari", "081211110004", "dewi@mail.com",
                                 "dewi123", "yuyun yuningsih", date(2002, 11, 30), "vip")
    rizky = User_NasabahPrioritas("rizky ramadhan", "081211110005", "rizky@mail.com",
                                  "rizky123", "tuti alawiyah", date(2001, 1, 8), "luxuryvvip")
    return [budi, siti, andi, dewi, rizky]


def _tab(no_rek, saldo, bunga, tgl):
    # bunga khusus per rekening; saldo minimum memakai default produk
    return Rekening_Tabungan(no_rek, saldo, tgl, bunga=bunga)


def _giro(no_rek, saldo):
    # biaya admin 10.000, batas pengambilan 200.000
    return Rekening_Giro(no_rek, saldo)


def buat_data():
    admin = _buat_admin()
    nasabah = _buat_nasabah()

    # rekening tiap nasabah (tabungan dan giro dicampur): total 8 tabungan + 5 giro
    rekening_per_nasabah = [
        # budi
        [_tab("1001", 1_000_000, 0.03, date(2025, 1, 10)),
         _tab("1002", 2_500_000, 0.03, date(2025, 2, 11)),
         _giro("2001", 500_000)],
        # siti
        [_tab("1003", 5_000_000, 0.04, date(2025, 1, 20)),
         _giro("2002", 1_500_000),
         _tab("1004", 750_000, 0.03, date(2025, 3, 5))],
        # andi
        [_tab("1005", 300_000, 0.02, date(2025, 4, 1)),
         _giro("2003", 800_000)],
        # dewi
        [_tab("1006", 3_200_000, 0.03, date(2025, 2, 25)),
         _tab("1007", 900_000, 0.03, date(2025, 5, 9)),
         _giro("2004", 2_000_000)],
        # rizky
        [_tab("1008", 10_000_000, 0.05, date(2025, 6, 15)),
         _giro("2005", 4_000_000)],
    ]

    # pasangkan: setiap rekening dibuka oleh nasabahnya
    semua_rekening = []
    for n, daftar in zip(nasabah, rekening_per_nasabah):
        for r in daftar:
            n.buka_rekening(r)
            semua_rekening.append(r)

    return admin, nasabah, semua_rekening