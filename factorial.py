def calculator_factorial(n):
    if n < 0:
        return "Факторіал не визначений для від’ємних чисел."
    result = 1
    for i in range(1,n +1):
        result *= i
    return result

if __name__== "__main__":
    try:
        number = int(input("Введіть ціле число: "))
        print(f"Факторіал числа {number} дорівнює {calculator_factorial(number)}")
    except ValueError:
        print("Помилка: введіть ціле число щоб програма могла зробити розрахкнок факторіалу.")
            

#fghhmhkfgophfg,o-pnurgfsdmynf
#fghhmhkfgophfg,o-pnurgfsdmynf#fghhmhkfgophfg,o-pnurgfsdmynf
#fghhmhkfgophfg,o-pnurgfsdmynf
#fghhmhkfgophfg,o-pnurgfsdmynf#fghhmhkfgophfg,o-pnurgfsdmynf