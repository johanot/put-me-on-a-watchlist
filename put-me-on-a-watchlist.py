#!/usr/bin/python
# -*- coding: utf-8 -*-
# browser history noise
import sys, requests

number_of_requests = 0

noise = [
    'how to make a bomb',
    'am i a psychopath',
    'how to become a terrorist',
    'am i being watched',
    'hydrogen bomb how',
    'lol nsa',
    'zoophilia forum',
    'am i a nazi',
    'why are jews bad',
    'i want to kill everyone is this normal',
    'pedo porn',
    'loli porn',
    'how do i doxx someone',
    'how do i hack the mainframe',
    'how to hack into the government',
    'how do i stage a coup',
    'buy guns where',
    'how to fire rifle',
    'shooting guns how',
    'how to create atom bomb',
    'staging a terrorist attack for dummies',
    'buy cocaine online',
    'buy heroin online',
    'buy illegal drugs online',
    'silk road 2.0',
    'silk road',
    'the dark web',
    'criminal stuff',
    'how to pick a lock',
    'how to dispose of a body',
    'uzi purchase online',
    'how to make a grenade',
    'buy shotgun with cash',
    'killing people bad?',
]
noise_length = len(noise)

while True:
    # Select query
    query = noise[number_of_requests % noise_length]

    # Clear screen
    print(chr(27) + "[2J")

    # Set up message
    number_of_requests += 1
    noun = 'requests' if number_of_requests > 1 else 'request'

    # Display message
    print("👩‍💻 put-me-on-a-watchlist.py")
    print("~~~")
    print("We're gonna do some dubious Google searches for you. Sit tight.")
    print("Feel free to run this process in the background.\n")
    print(
        "Made %d %s. Press CTRL + C to stop" %
        (number_of_requests, noun)
    )
    print("\tSearched for \"%s\"" % query)

    # Make the request
    try:
        requests.get("http://google.com/?q=%s" % query)
    except (KeyboardInterrupt, SystemExit):
        print(
            "\n\t%d %s made in total. Bye!" %
            (number_of_requests, noun)
        )
        sys.exit()
