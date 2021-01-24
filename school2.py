fibonacci_list = list()


def fibonacci_sequence_generator(n):
    num1, num2 = 0, 1
    count = 0
    if n <= 0:
        print("use a positive number...")
        quit()
    else:
        while count < n:
            fibonacci_list.append(num1)
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            count += 1
