class User:
    __count = 0
    def __init__(self, id_user, nama, no_hp, email, password):
        self.__id_user = id_user
        self.__password = password
        self.__nama = None
        self.__no_hp = None
        self.__email = None
        self.set_nama(nama)
        self.set_no_hp(no_hp)
        self.set_email(email)
        
# getter
    def get_id_user(self):
        return self.__id_user

    def get_nama(self):
        return self.__nama

    def get_no_hp(self):
        return self.__no_hp

    def get_email(self):
        return self.__email
    # def get_pw(self):
    #     return self.__password
    
# setter
    def set_nama(self,nama):
        self.__nama = nama.strip().title()

    def set_no_hp(self,no_hp):
        self.__no_hp = no_hp

    def set_email(self, email):
        val = lambda e: "@" in e and "." in e
        if not val(email):
            raise ValueError("format tidak sesuai".title())
        self.__email = email

# fungsi lainnya
    def login(self, email, password): 
        if self.get_email() == email and self.__password == password:
            print(f"Selamat datang {self.get_nama()}")
            return True
        print(f"email atau password tidak sesuai !".title())
        return False

    def lihat_profil(self):
        print(f"\nNama : {self.get_nama()}")
        print(f"Nomor Hp : {self.get_no_hp()}")
        print(f"Email : {self.get_email()}")