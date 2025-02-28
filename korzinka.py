from uuid import uuid4
from collections import namedtuple

Mahsulot = namedtuple("Mahsulot", ["nomi", "narxi", "miqdor"])

class Basket:
    def __init__(self):
        self.savat = {}
        self.savat2 = {}

    def mahsulot_qosh(self, nomi: str, narxi: int, miqdor: int = 1) -> str:
        mahsulot_id = str(uuid4())
        self.savat[mahsulot_id] = Mahsulot(nomi, narxi, miqdor)
        return mahsulot_id

    def mahsulot_olib_tashla(self, mahsulot_id: str, miqdor: int = 1) -> None:
        if mahsulot_id in self.savat:
            mahsulot = self.savat[mahsulot_id]
            if mahsulot.miqdor > miqdor:
                self.savat[mahsulot_id] = Mahsulot(mahsulot.nomi, mahsulot.narxi, mahsulot.miqdor - miqdor)
            else:
                del self.savat[mahsulot_id]

    def hisobla(self) -> int:
        return sum(m.narxi * m.miqdor for m in self.savat.values())

    def korish(self) -> None:
        if not self.savat:
            print("Savatcha bo'sh!")
            return
        print("Savatcha tarkibi:")
        for mahsulot_id, m in self.savat.items():
            print(f"{m.nomi} - {m.miqdor} dona x {m.narxi} so'm (ID: {mahsulot_id})")
        print(f"Jami summa: {self.hisobla()} so'm\n")

    def ikkinchi_savatga_otkazish(self) -> None:
        self.savat2 = self.savat.copy()

    def ikkinchi_savatni_tozalash(self) -> None:
        self.savat2.clear()

    def barcha_savatni_tozalash(self) -> None:
        self.savat.clear()
        self.savat2.clear()

savat = Basket()
mahsulotlar = {
    "Non": (4000, 2), "Sut": (12000, 1), "Shakar": (18000, 3), "Tuz": (5000, 1), "Go'sht": (70000, 2),
    "Piyoz": (3000, 5), "Kartoshka": (2500, 4), "Sabzi": (2000, 3), "Olma": (10000, 2), "Banan": (15000, 3),
    "Un": (22000, 1), "Yog'": (25000, 2), "Tuxum": (12000, 1), "Qand": (9000, 2), "Kolbasa": (45000, 1),
    "Pechenye": (12000, 2), "Makaron": (8000, 3), "Tvorog": (15000, 1), "Smetana": (18000, 2), "Sharbat": (14000, 1)
}

mahsulot_idlar = {nomi: savat.mahsulot_qosh(nomi, narxi, miqdor) for nomi, (narxi, miqdor) in mahsulotlar.items()}
savat.korish()
savat.mahsulot_olib_tashla(mahsulot_idlar["Non"], 1)
savat.korish()
savat.ikkinchi_savatga_otkazish()
savat.ikkinchi_savatni_tozalash()
savat.barcha_savatni_tozalash()
