from modul import *


products = [
    Food("Olma", 2, 50, "2025-05-10"),
    Electronics("Noutbuk", 1000, 5, 2)
]


while True:
    print("\n1. Mahsulot sotish\n2. Mahsulotlar ro‘yxati\n3. Chiqish")
    choice = input("Tanlang: ")
    
    if choice == "1":
        for i, product in enumerate(products):
            print(f"{i + 1}. {product.name} - {product.price}$ ({product.quantity} dona)")
        prod_index = int(input("Mahsulot tanlang (raqamini kiriting): ")) - 1
        amount = int(input("Nechta sotmoqchisiz? "))
        print(products[prod_index].sell(amount))
    
    elif choice == "2":
        for product in products:
            print(f"{product.name}: {product.price}$ ({product.quantity} dona)")
    
    elif choice == "3":
        print("Dastur yakunlandi!")
        break
    
    else:
        print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")