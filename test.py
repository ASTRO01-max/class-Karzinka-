data = [
    ["Ism", "Yosh", "Kasb"],
    ["Ali", 25, "Dasturchi"],
    ["Vali", 30, "Muhandis"],
    ["Hasan", 22, "O'qituvchi"],
    ["Husan", 28, "Shifokor"]
]

with open("test.csv", "w", encoding="utf-8") as file:
    for row in data:
        file.write(",".join(map(str, row)) + "\n")

print("CSV faylga saqlandi! Excel'da ochib ko'ring.")