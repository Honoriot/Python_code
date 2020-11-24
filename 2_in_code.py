import random
import time

Mode = {
        "1" : "Reapeat List",
        "2" : "Random",
        "3" : "Reapat This",
        }

Music_list = ["Music1", "Music2", "Music3", "Music4", "Music5"]

def entry_point(Music_list):
        print("Playlist: ")
        for x in Music_list:
                print(x)
        Play = input("Enter 'P' to play and 'S' to stop: ")
        if Play == 'p' or Play == "P":
                select_mode(Mode)
        elif Play == 'S' or Play == 's':
                print("Thanks for your response, press any to exit")
                input("")
                exit()

def select_mode(Mode):
        print("The modes available to play the song:")
        for x in Mode:
                print(x)
        select_mode = input("Choose a mode from the above: ")
        if select_mode in Mode:
                return select_mode
        else:
                print("Not a good select, select again: ")
                select_mode()

def Play(mode):
        if mode == "1": # Play list
                for x in Music_list:
                        print("Playing: " + x)
                        time.sleep(4)
        elif mode == "2": # play random
                position = []
                for x in range(len(Music_list)):
                        current_position = random.randint(0, len(Music_list)-1)
                        while current_position in position:
                                current_position = random.randint(0, 3)
                        position.append(current_position)
                        print("Playing: " + Music_list[current_position])
                        time.sleep(4)
        elif mode == "3": # Repeat one song
                Select_song = input("Enter the song want to play according to position value start from '1': ")
                if Select_song <= len(Music_list):
                        for x in range(4):
                                print("Playing: " + Music_list[Select_song-1])
                                time.sleep(4)
                else:
                        print("Selected music not present: ")

Play("2")