# Конвертирование мили в км
def convert(miles):
    miles = input("Введите мили: ")
    return int(miles) * 1.609344


a = convert(2)
print(str(a) + " км")
