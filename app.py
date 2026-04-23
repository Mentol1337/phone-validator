from validator import validate_phone

def main():
    phone = input("Введіть номер: ")

    try:
        if validate_phone(phone):
            print("Номер правильний ✅")
        else:
            print("Номер неправильний ❌")
    except ValueError as e:
        print("Помилка:", e)

if __name__ == "__main__":
    main()