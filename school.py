import random

Ticket_Price = 42
Glasses3D_Price = 5
# Taken from a top 20 songs of 2020 chart.
song_list = ["BLINDING LIGHTS", "DANCE MONKEY", "ROSES", "BEFORE YOU GO", "HEAD & HEART", "DON'T START NOW", "ROCKSTAR", "SOMEONE YOU LOVED", "	OWN IT", "WATERMELON SUGAR", "SAVAGE LOVE", "THE BOX", "SAY SO", "LONELY", "BREAKING ME", "ADORE YOU", "RAIN ON ME", "ROVER", "PHYSICAL", "MOOD"]
list2 = list()
fibonacci_list = list()


def Total_Price_Calculator(Ticket_Amount, Glasses3D_Amount):
    return Ticket_Price*Ticket_Amount+Glasses3D_Price*Glasses3D_Amount


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


def random_song_player(num_of_songs):
    if num_of_songs > 20:
        print("there are only 20 songs")
        quit()

    for i in range(0, num_of_songs):
        random_song = random.choice(song_list)
        song_list.pop(song_list.index(random_song))
        list2.append(random_song)


def menu(num):
    if num == 1:
        ticket_requested_amount = int(input("Enter Number of tickets: "))
        glasses3d_requested_amount = int(input("Enter Number of tickets: "))
        total_cost = Total_Price_Calculator(ticket_requested_amount, glasses3d_requested_amount)
        print("your total cost will be {}".format(total_cost))
    if num == 2:
        n = int(input("enter fibonacci sequence length: "))
        fibonacci_sequence_generator(n)
        print(fibonacci_list)
    if num == 3:
        num_of_songs = int(input("Enter number of songs: "))
        random_song_player(num_of_songs)
        print(list2)


menu_num = int(input("1) Total_Price_Calculator \n2) fibonacci_sequence_generator \n3) random_song_player \nEnter question number: "))
menu(menu_num)
