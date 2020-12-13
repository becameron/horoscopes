#!/usr/bin/python3


import json
import os
import random




with open('horoscopes.json','r') as file:
    horoscopes = json.load(file)

dict(horoscopes)

def HoroWriter(runfunc):

    while runfunc != 'y':
        print('''\nWelcome to the HoroWriter, you can retrive old horoscopes from other days
        or make new horoscopes from old data.\n''')

        sign = input('What is your sign? ').lower()


        if sign not in horoscopes:
            exitfunc()
            return

        decision = input('\n Do you want to retrieve an old horoscope or create new one? (old/new) ').lower()
        if decision == 'old':
            old_horo(sign)
            return

        elif decision == 'new':
            new_horo(sign)
            return


def old_horo(sign):

        #creates a list of dates and sorts them
        dates = set()
        for date in horoscopes[sign].keys():
            dates.add(date)
        dates = list(dates)
        dates.sort()


        #shows a listing of all the dates available
        print('The following dates are available for horoscopes: \n')

        for date in dates:
            print(date)

        response = input('\nPlease enter the date you are interested in: ')
        if response in dates:
            print('\n'+horoscopes[sign][response]+'\n')

        elif response == '':
            exitfunc()

        else:
            print('\nPlease select another date.\n')
            old_horo(sign)


def new_horo(sign):

        #splits each date entry for a sign apart by sentences

        generator = []

        for date in horoscopes[sign].keys():
            generator = horoscopes[sign][date].split('.') + generator

        #determines the largest number in the generator list
        limit = len(generator)

        #standardizes the length of the new horoscope to be between 3 and 8 sentences long.
        sentences = random.randrange(3,8)

        #writes the new horoscope by recombining the old horoscope.
        message = ''

        for i in range(sentences):
            message = generator[random.randrange(0,limit)]+'. '+message

        print('\n'+message+'\n')
        exitfunc()

def exitfunc():
    answer = input('\nDo you want to quit? (y/n)\n')
    if answer == 'y' or answer == '':
        print('\ngoodbye.')
        HoroWriter('y')

    if answer == 'n':
        HoroWriter('n')

HoroWriter('n')
