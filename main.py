def add(a, b):
    return a + b


     

def display_menu():
    print("Выберите операцию:")
    print("1. Сложение")
    
    print("0. Выход")

def main():
    while True:
        display_menu()
        choice = input("Введите номер операции (или 0 для выхода): ")

        if choice == '0':
            print("Программа завершена.")
            break
        elif choice == '1':
            num1, num2 = map(float, input("Введите два числа через пробел: ").split())
            print("Результат сложения:", add(num1, num2))
        
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
