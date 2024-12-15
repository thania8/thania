class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def informasi(self):
        print("Nama\t\t\t:", self.nama)
        print("Makanan\t\t\t:", self.makanan)
        print("Habitat\t\t\t:", self.hidup)
        print("Berkembang Biak\t\t:", self.berkembang_biak)