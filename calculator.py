# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def calc(NUM_1, NUM_2, COMMAND):
    if COMMAND == '+':
        return NUM_1 + NUM_2

    elif COMMAND == '-':
        return NUM_1 - NUM_2

    elif COMMAND == 'x':
        return NUM_1 * NUM_2

    elif COMMAND == '/':
        return NUM_1 / NUM_2

    elif COMMAND == 'pwr':
        return NUM_1 ** NUM_2

    elif COMMAND == 'sin':
        return (math.sin(NUM_1))

    elif COMMAND == 'cos':
        return (math.cos(NUM_1))

    elif COMMAND == 'tan':
        return (math.tan(NUM_1))

    elif COMMAND == 'log':
        return (math.log(NUM_1 , NUM_2))

    elif COMMAND == 'natural log':
        return (math.log(NUM_1))

    else:
        return f"Пошел н@*#й, это не команда: {COMMAND!r}."


if __name__ == '__main__':
  while True: # программа выполняется до ввода 0 вместо
    COMMAND = input("Введите операцию > ")
    if COMMAND.isdigit() and int(COMMAND) == 0:
        break
    NUM_1 = float(input("первое число > "))
    NUM_2 = float(input("второе число > "))
    print(calc(NUM_1, NUM_2, COMMAND))
