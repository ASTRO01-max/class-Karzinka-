from abc import ABC, abstractmethod
from uuid import uuid4
from datetime import datetime

class Product(ABC):
    def __init__(self, name, price, quantity):
        self.name = name  
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def sell(self, amount):
        pass

    @abstractmethod
    def restock(self, amount):
        pass

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty, brand):
        super().__init__(name, price, quantity)
        self.warranty = warranty
        self.brand = brand
        self.__e_id = uuid4()  

    def info(self):
        return (f"Brendi: {self.brand}, Nomi: {self.name}, Narxi: {self.price}, "
                f"Soni: {self.quantity}, Garantiya: {self.warranty}, ID: {self.__e_id}")

    def sell(self, amount):
        if amount > self.quantity:
            return f"Xatolik: Omborda faqat {self.quantity} dona bor!"
        self.quantity -= amount
        return f"{amount} dona {self.name} sotildi. Omborda qolgan: {self.quantity}"

    def restock(self, amount):
        self.quantity += amount
        return f"{amount} dona {self.name} omborga qo'shildi. Yangi soni: {self.quantity}"

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

    def info(self):
        return (f"Nomi: {self.name}, Narxi: {self.price}, Soni: {self.quantity}, "
                f"Muddati: {self.expiration_date.strftime('%Y-%m-%d')}")

    def sell(self, amount):
        if self.expiration_date < datetime.now(): 
            return "Xatolik: mahsulot muddati o'tgan!"
        if amount > self.quantity:
            return f"Xatolik: Omborda faqat {self.quantity} dona bor!"
        self.quantity -= amount
        return f"{amount} dona {self.name} sotildi. Omborda qolgan: {self.quantity}"

    def restock(self, amount):
        self.quantity += amount
        return f"{amount} dona {self.name} omborga qo'shildi. Yangi soni: {self.quantity}"

class Household(Product):
    def __init__(self, name, price, quantity, material, size, brand=None):
        super().__init__(name, price, quantity)
        self.material = material  
        self.size = size  
        self.brand = brand

    def info(self):
        brand_info = f", Brend: {self.brand}" if self.brand else ""
        return (f"Nomi: {self.name}, Narxi: {self.price}$, Soni: {self.quantity}, "
                f"Material: {self.material}, O'lchami: {self.size}{brand_info}")

    def sell(self, amount):
        if amount > self.quantity:
            return f"Xatolik: Omborda faqat {self.quantity} dona bor!"
        self.quantity -= amount
        return f"{amount} dona {self.name} sotildi. Omborda qolgan: {self.quantity}"

    def restock(self, amount):
        self.quantity += amount
        return f"{amount} dona {self.name} omborga qo'shildi. Yangi soni: {self.quantity}"

    def clean_instructions(self):
        if self.material.lower() in ["plastmassa", "shisha", "keramika"]:
            return "Nam mato bilan artish tavsiya etiladi."
        elif self.material.lower() in ["mato", "yog'och"]:
            return "Quruq shimgich yoki maxsus vosita bilan tozalash tavsiya etiladi."
        return "Tozalash bo'yicha maxsus tavsiyalar yo'q."

    
class Manageproduct:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        return f"{product.name} omborga qo'shildi."
    
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return f"{product_name} ombordan olib tashlandi."
        return "Mahsulot topilmadi."
    
    def list_products(self):
        if not self.products:
            return "Omborda hech qanday mahsulot yo'q."
        return "\n".join([product.info() for product in self.products])
    
    def check_stock(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return f"{product_name} dan {product.quantity} dona omborda mavjud."
        return "Mahsulot topilmadi."

class Parking:
    def __init__(self, residence, num):
        self.residence = residence
        self.num = num
        self.__r_id = uuid4()
        self.lst = []

    def parking(self):
        if self.num in self.lst:
            return "Bu joy band!"
        else:
            self.lst.append(self.num)
            return (f"Turar joy nomi: {self.residence}, "
                    f"turar joy raqami: {self.num}, "
                    f"turar joy id raqami: {self.__r_id}")

class SecurityCamera:
    def __init__(self, brand, resolution, night_vision=False, motion_detection=False):
        self.camera_id = uuid4()
        self.brand = brand
        self.resolution = resolution
        self.night_vision = night_vision
        self.motion_detection = motion_detection
        self.is_recording = False
        self.last_recorded_time = None

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.last_recorded_time = datetime.now()
            return f"{self.brand} kamerasi yozib olishni boshladi ({self.last_recorded_time.strftime('%Y-%m-%d %H:%M:%S')})."
        return "Kamera allaqachon yozib olmoqda."

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            return f"{self.brand} kamerasi yozib olishni to'xtatdi."
        return "Kamera hozir yozib olayotgani yo'q."

    def get_status(self):
        status = "Yozib olmoqda" if self.is_recording else "Yozib olayotgani yo'q"
        features = [
            f"Brend: {self.brand}",
            f"Ruxsat berish qobiliyati: {self.resolution}",
            f"Tungi ko'rish: {'Bor' if self.night_vision else "Yo'q"}",
            f"Harakatni aniqlash: {'Bor' if self.motion_detection else "Yo'q"}",
            f"Hozirgi holat: {status}",
        ]
        return "\n".join(features)


class Payment(ABC):
    def __init__(self, payment):
        self.payment = payment
    
    @abstractmethod
    def process_payment(self):
        pass

class BankPayment(Payment):
    def __init__(self, payment, bank_name, account_num = 5000000):
        super().__init__(payment)
        self.bank_name = bank_name
        self.account_num = account_num

    def process_payment(self, product):
        if self.account_num < product:
            return "xisobingizda yetarlicha pul yo'q!"
        else:
            return f"Bank nomi: {self.bank_name}, hisob raqami: {self.account_num}, to'lov miqdori: {self.payment}"

    def check_balance(self):
        return f"Hisobingizda: {self.account_num} so'm miqdorda opul bor"

class CashPayment(Payment):
    def __init__(self, payment, cash=500000, currency="UZS"):
        super().__init__(payment)
        self.cash = cash
        self.currency = currency

    def process_payment(self, product):
        if self.cash < product:
            return "Yetarlicha pul yo'q!"
        else:
            self.cash -= product
            return f"{product} {self.currency} to'landi, qoldiq: {self.cash} {self.currency}"

    def add_cash(self, amount):
        self.cash += amount
        return f"Kassaga {amount} {self.currency} qo'shildi. Joriy balans: {self.cash} {self.currency}"

    def check_cash_balance(self):
        return f"Kassadagi mavjud mablag': {self.cash} {self.currency}"

class ShoppingReceipt:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        self.receipt = []
    
    def add_purchase(self, product_name, price):
        payment_result = self.payment_method.process_payment(price)
        if "to'landi" in payment_result:
            transaction_id = str(uuid4())
            self.receipt.append({"id": transaction_id, "product": product_name, "price": price})
            return f"Xarid muvaffaqiyatli amalga oshirildi! ID: {transaction_id}\n{payment_result}"
        return payment_result
    
    def print_receipt(self):
        if not self.receipt:
            return "Hech qanday xarid amalga oshirilmagan!"
        receipt_str = "*** Xaridlar kvitansiyasi ***\n"
        for item in self.receipt:
            receipt_str += f"ID: {item['id']}\nMahsulot: {item['product']}\nNarx: {item['price']} UZS\n--------------------------\n"
        return receipt_str

class Person(ABC):
    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.w_id = str(uuid4())
        self.phone = None
        self.email = None
        self.work_hours = 0
        self.tasks = []

    @abstractmethod
    def add_work_hours(self, hours):
        pass

    @abstractmethod
    def assign_task(self, task):
        pass

    def get_info(self):
        return {
            "ID": self.w_id,
            "Name": self.name,
            "Surname": self.surname,
            "Position": self.position,
            "Salary": self.salary,
            "Phone": self.phone if self.phone else "Noma'lum",
            "Email": self.email if self.email else "Noma'lum",
            "Work Hours": self.work_hours,
            "Tasks": self.tasks
        }

class Paymaster(Person):
    def __init__(self, name, surname, position, salary, cash_register):
        super().__init__(name, surname, position, salary)
        self.cash_register = cash_register

    def add_work_hours(self, hours):
        if hours > 0:
            self.work_hours += hours

    def assign_task(self, task):
        self.tasks.append(task)

    def process_payment(self, amount):
        if amount > 0 and self.cash_register >= amount:
            self.cash_register -= amount
            return f"{amount} so'm to'lov amalga oshirildi. Qoldiq: {self.cash_register} so'm."
        return "Xatolik! Yetarli mablag' yo'q yoki noto'g'ri summa kiritildi."

    def generate_salary_report(self, workers):
        report = {"Total Salary": 0, "Workers": []}
        for worker in workers:
            report["Workers"].append({
                "Name": worker.name,
                "Surname": worker.surname,
                "Position": worker.position,
                "Salary": worker.salary
            })
            report["Total Salary"] += worker.salary
        return report

    def audit_cash_register(self):
        expected_balance = self.salary * 10
        if self.cash_register < expected_balance:
            return f"Kassada {expected_balance - self.cash_register} so'm yetishmovchilik bor!"
        elif self.cash_register > expected_balance:
            return f"Kassada {self.cash_register - expected_balance} so'm ortiqcha bor!"
        return "Kassa balansida muammo yo'q."

class Cleaner(Person):
    def __init__(self, name, surname, position, salary, area_responsible):
        super().__init__(name, surname, position, salary)
        self.area_responsible = area_responsible
        self.cleaned_areas = []

    def add_work_hours(self, hours):
        if hours > 0:
            self.work_hours += hours

    def assign_task(self, task):
        self.tasks.append(task)

    def clean_area(self, area):
        self.cleaned_areas.append(area)
        return f"{self.name} {area} hududini tozaladi."

    def get_cleaning_report(self):
        return {
            "Cleaner": f"{self.name} {self.surname}",
            "Areas Cleaned": self.cleaned_areas
        }

class Management:
    def __init__(self, name, fam, category):
        self.name = name
        self.fam = fam
        self.category = category
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        return f"{employee.name} {employee.surname} tizimga qo'shildi."

    def remove_employee(self, employee_id):
        for emp in self.employees:
            if emp.w_id == employee_id:
                self.employees.remove(emp)
                return f"{emp.name} {emp.surname} tizimdan o'chirildi."
        return "Xodim topilmadi."

    def list_employees(self):
        if not self.employees:
            return "Hozircha hech qanday xodim mavjud emas."
        return [emp.get_info() for emp in self.employees]

    def total_salary_expense(self):
        return sum(emp.salary for emp in self.employees)

    def assign_task_to_employee(self, employee_id, task):
        for emp in self.employees:
            if emp.w_id == employee_id:
                emp.assign_task(task)
                return f"{task} vazifasi {emp.name} {emp.surname} ga biriktirildi."
        return "Xodim topilmadi."

class Basket:
    def __init__(self):
        self.savat = {}  
        self.savat2 = {} 

    def mahsulot_qosh(self, nomi, narxi, miqdor=1):
        mahsulot_id = str(uuid4())  
        self.savat[mahsulot_id] = (nomi, narxi, miqdor)
        print(f" {nomi} ({miqdor} dona) savatchaga qo'shildi. ID: {mahsulot_id}")
        return mahsulot_id

    def mahsulot_olib_tashla(self, mahsulot_id, miqdor=1):
        if mahsulot_id in self.savat:
            nomi, narxi, mavjud_miqdor = self.savat[mahsulot_id]
            if mavjud_miqdor > miqdor:
                self.savat[mahsulot_id] = (nomi, narxi, mavjud_miqdor - miqdor)
            else:
                del self.savat[mahsulot_id]
            print(f" {nomi} ({miqdor} dona) savatdan olib tashlandi.")
        else:
            print(f" ID {mahsulot_id} bo'yicha mahsulot savatchada yo'q!")

    def hisobla(self):
        jami_summa = sum(narx * miqdor for _, narx, miqdor in self.savat.values())
        return jami_summa

    def korish(self):
        if not self.savat:
            print(" Savatcha bo'sh!")
        else:
            print("\n Savatcha tarkibi:")
            for mahsulot_id, (nomi, narxi, miqdor) in self.savat.items():
                print(f"- {mahsulot_id}: {nomi} - {miqdor} dona x {narxi} so'm")
            print(f" Jami summa: {self.hisobla()} so'm\n")

    def ikkinchi_savatga_otkazish(self):
        self.savat2 = self.savat.copy()
        print(" Mahsulotlar 2-chi savatchaga o'tkazildi.")

    def ikkinchi_savatni_tozalash(self):
        self.savat2.clear()
        print(" Ikkinchi savatcha butunlay o'chirildi.")

    def barcha_savatni_tozalash(self):
        self.savat.clear()
        self.savat2.clear()
        print(" Barcha savatlar tozalandi!")
        