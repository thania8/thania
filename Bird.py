class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print("Nama\t\t\t:", self.nama)
        print("Makanan\t\t\t:", self.makanan)
        print("Habitat\t\t\t:", self.hidup)
        print("Berkembang Biak\t\t:", self.berkembang_biak)

class Bird(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    def info_bird(self):
        super().info_animal()
        print("Warna\t\t\t:", self.warna)
        print("Jenis Paruh\t\t:", self.paruh)

# Objek
print()
bird = Bird("Elang", "Daging", "Ditebing", "menghasilkan telur", "coklat", "bengkok dan lancip")
print("## Info Bird ##")
bird.info_bird()