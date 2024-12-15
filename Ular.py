from Animal import animal

class Ular(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat

    def info_ular(self):
        super().informasi()
        print("Bernapas menggunakan\t: ", self.bernapas,
            "\nHabitat Di\t\t: ", self.habitat)

#objek
print()
ular = Ular("Kobra", "Tikus", "Aktif pada siang atau malam hari", "Bertelur", "Paru-Paru", "Hutan")
print("===================================================")
print("## Infp ular ##")
ular.info_ular()

print()
ular = Ular("Piton", "Hewan kecil hingga besar", "Ular piton melilit mangsanya hingga mati sebelum menelannya utuh", "Bertelur", "Paru-Paru", "Hutan")
print("===================================================")
print("## Infp ular ##")
ular.info_ular()

print()
ular = Ular("sanca", "Mamalia kecil, burung, dan reptil kecil", "Melilit mangsanya untuk membunuh sebelum menelannya", "Bertelur", "Paru-Paru", "Daerah dekat sungai")
print("===================================================")
print("## Infp ular ##")
ular.info_ular()
