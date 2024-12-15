from Animal import animal

class Fish(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat

    def info_fish(self):
        super().informasi()
        print("Bernapas menggunakan\t: ", self.bernapas,
            "\nHabitat Di\t\t: ", self.habitat)

#objek
print()
fish = Fish("Hiu", "Karnivora; memakan ikan kecil", "Predator puncak yang berenang aktif untuk mencari mangsa", "Bertelur dan Melahirkan", "Insang", "Laut")
print("===================================================")
print("## Infp Fish ##")
fish.info_fish()
print()
fish = Fish("KOI", "Omnivora; memakan plankton", "Hidup di air tawar yang tenang", "Bertelur", "Insang", "Kolam")
print("===================================================")
print("## Infp Fish ##")
fish.info_fish()
print()
fish = Fish("Cupang", " Karnivora; memakan larva serangga", " Hidup soliter dan teritorial", "Bertelur", "Insang", "Perairan tawar seperti kolam kecil")
print("===================================================")
print("## Infp Fish ##")
fish.info_fish()