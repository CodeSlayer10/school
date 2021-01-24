import random


# Taken from a top 20 songs of 2020 chart.
song_list = ["BLINDING LIGHTS", "DANCE MONKEY", "ROSES", "BEFORE YOU GO", "HEAD & HEART", "DON'T START NOW", "ROCKSTAR", "SOMEONE YOU LOVED", "OWN IT", "WATERMELON SUGAR", "SAVAGE LOVE", "THE BOX", "SAY SO", "LONELY", "BREAKING ME", "ADORE YOU", "RAIN ON ME", "ROVER", "PHYSICAL", "MOOD"]
list2 = list()


def random_song_player(num_of_songs):
    if num_of_songs > 20:
        print("there are only 20 songs")
        quit()

    for i in range(0, num_of_songs):
        random_song = random.choice(song_list)
        song_list.pop(song_list.index(random_song))
        list2.append(random_song)


num_of_songs = int(input("Enter number of songs: "))
random_song_player(num_of_songs)
print(list2)
