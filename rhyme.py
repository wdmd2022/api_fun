#!/usr/bin/python3
"""got rhymes?"""

import requests
import sys
import time
import os

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("COME ON! JUST GIVE ME A SINGLE WORD TO RHYME")
        quit()

    os.system('cls' if os.name == 'nt' else 'clear')
    ll_cool_word = sys.argv[1]
    print("\u0332".join("Welcome to RhymeBot 3000"))
    time.sleep(1)
    print("I am a robot that helps your poems be good")
    time.sleep(2)
    print("Prepare for the best rhymes of your life")
    time.sleep(1)
    print("")
    print("...................")
    print("")
    print("fetching rhymes for '{}' as requested...".format(ll_cool_word))
    time.sleep(2)
    print("hold on, still thinking...")
    time.sleep(1)
    print("please be patient, rhymes are hard")
    time.sleep(3)
    print("")
    print("okay, here you go:")
    print(".................")
    
    ll_cool_request = "https://rhymebrain.com/talk?function=getRhymes&word={}".format(ll_cool_word)
    r = requests.get(ll_cool_request)
    rhymez_dict = r.json()
    for each_cool_rhyme in rhymez_dict:
        if each_cool_rhyme["score"] > 275:
            print(each_cool_rhyme["word"])
            time.sleep(1)
            print("...")
    print("...")
    print("umm....")
    print("")
    print(".................")
    print("that's all I got. Hope your poem goes well!")
    print("")
    print("")
    print("")
    time.sleep(4)
    print("... and I hope you can forgive yourself for cheating")
    print("")
