from modul import *
from uuid import uuid4
import json

basket = Basket()
management = Management("Admin", "Adminov", "Manager")


products = [
    Food("Olma", 2, 50, "2025-05-10"),
    Electronics("Noutbuk", 1000, 5, 2, "HP")
]

path = "order.json"

def read():
    with open(path, "r") as file:
        data = json.load(file)
    return data

def write(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

receipt = None

menu = ("\nMenyudan birini tanlang:\n"
      "1. Mahsulot sotish\n"
      "2. Mahsulotlar ro'yxatini ko'rish\n"
      "3. Avtoturargoh holatini ko'rish\n"
      "4. Xavfsizlik kamerasi sozlamalari\n"
      "5. Bank orqali to'lov qilish\n"
      "6. Naqd pul orqali to'lov qilish\n"
      "7. Xarid qilish\n"
      "8. Balansni tekshirish\n"
      "9. Kvitasiyani ko'rish\n"
      "10. Yangi xodim qo'shish\n"
      "11. Xodimni o'chirish\n"
      "12. Xodimlarni ko'rish\n"
      "13. Xodimga vazifa biriktirish\n"
      "14. Mahsulot qo'shish\n"
      "15. Mahsulot olib tashlash\n"
      "16. Savatchani ko'rish\n"
      "17. Savatchani tozalash\n"
      "18. Chiqish")

while True:
    print(menu)

    choice = input("Tanlovingizni kiriting: ")

    if choice == "1":
        for i, product in enumerate(products):
            print(f"{i + 1}. {product.name} - {product.price}$ ({product.quantity} dona)")

        try:
            prod_index = int(input("Mahsulot tanlang (raqamini kiriting): ")) - 1
            if prod_index < 0 or prod_index >= len(products):
                print("Noto'g'ri raqam tanlandi!")
                continue

            amount = int(input("Nechta sotmoqchisiz? "))
            print(products[prod_index].sell(amount))
        except ValueError:
            print("Iltimos, raqam kiriting!")

    elif choice == "2":
        for product in products:
            print(f"{product.name}: {product.price}$ ({product.quantity} dona)")

    elif choice == "3":
        residence = input("Turar joy nomini kiriting: ")
        num = input("Turar joy raqamini kiriting: ")
        parking_spot = Parking(residence, num)
        print(parking_spot.parking())

    elif choice == "4":
        brand = input("Kamera brendini kiriting: ")
        resolution = input("Ruxsat berish qobiliyatini kiriting (masalan, 1080p): ")
        night_vision = input("Tungi ko'rish mavjudmi? (ha/yo'q): ").strip().lower() == "ha"
        motion_detection = input("Harakatni aniqlash mavjudmi? (ha/yo'q): ").strip().lower() == "ha"

        camera = SecurityCamera(brand, resolution, night_vision, motion_detection)

        while True:
            print("\n1. Yozib olishni boshlash\n2. Yozib olishni to'xtatish\n3. Kamera holatini ko'rish\n4. Orqaga qaytish")
            cam_choice = input("Tanlovingizni kiriting: ")

            if cam_choice == "1":
                print(camera.start_recording())
            elif cam_choice == "2":
                print(camera.stop_recording())
            elif cam_choice == "3":
                print(camera.get_status())
            elif cam_choice == "4":
                break
            else:
                print("Noto'g'ri tanlov! Qayta urinib ko'ring.")

    elif choice == "5":
        bank_name = input("Bank nomini kiriting: ")
        try:
            account_balance = int(input("Hisob raqamdagi mablag'ni kiriting: "))
            bank_payment = BankPayment(0, bank_name, account_balance)
            receipt = ShoppingReceipt(bank_payment)
            print("Bank orqali to'lov usuli tanlandi.")
        except ValueError:
            print("Noto'g'ri mablag' miqdori!")

    elif choice == "6":
        try:
            cash_balance = int(input("Kassadagi mablag'ni kiriting: "))
            cash_payment = CashPayment(0, cash_balance)
            receipt = ShoppingReceipt(cash_payment)
            print("Naqd pul orqali to'lov usuli tanlandi.")
        except ValueError:
            print("Noto'g'ri mablag' miqdori!")

    elif choice == "7":
        if not receipt:
            print("Avval to'lov usulini tanlang!")
            continue

        product_name = input("Mahsulot nomini kiriting: ")
        try:
            product_price = int(input("Mahsulot narxini kiriting: "))
            print(receipt.add_purchase(product_name, product_price))
        except ValueError:
            print("Noto'g'ri narx kiritildi!")

    elif choice == "8":
        if not receipt:
            print("Avval to'lov usulini tanlang!")
            continue

        if isinstance(receipt.payment_method, BankPayment):
            print(receipt.payment_method.check_balance())
        else:
            print(receipt.payment_method.check_cash_balance())

    elif choice == "9":
        if not receipt:
            print("Avval to'lov usulini tanlang!")
            continue
        print(receipt.print_receipt())

    elif choice == "10":
        name = input("Xodim ismi: ")
        surname = input("Xodim familiyasi: ")
        position = input("Xodim lavozimi: ")
        salary = int(input("Xodim maoshi: "))
        employee = Person(name, surname, position, salary)
        print(management.add_employee(employee))  

    elif choice == "11":
        emp_id = input("O'chirish uchun xodim ID sini kiriting: ")
        print(management.remove_employee(emp_id))

    elif choice == "12":
        employees = management.list_employees()
        for emp in employees:
            print(emp)

    elif choice == "13":
        emp_id = input("Vazifa berish uchun xodim ID sini kiriting: ")
        task = input("Vazifani kiriting: ")
        print(management.assign_task_to_employee(emp_id, task))
    
    elif choice == "14":
        nomi = input("Mahsulot nomi: ")
        narxi = int(input("Mahsulot narxi: "))
        miqdor = int(input("Mahsulot miqdori: "))
        basket.mahsulot_qosh(nomi, narxi, miqdor)
    
    elif choice == "15":
        mahsulot_id = input("Olib tashlash uchun mahsulot ID sini kiriting: ")
        miqdor = int(input("Miqdorini kiriting: "))
        basket.mahsulot_olib_tashla(mahsulot_id, miqdor)
    
    elif choice == "16":
        basket.korish()
    
    elif choice == "17":
        basket.barcha_savatni_tozalash()

    elif choice == "18":
        print("Dastur yakunlandi!")
        break

    else:
        print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")
