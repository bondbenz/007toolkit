#!/usr/bin/python
import urllib2
import re
import os
import random
import string
import itertools
from urlparse import urlparse

logo = """
##########################################################
#     ___   ___ _____    _____            _       _ _    #
#    / _ \ / _ \___  |  /__   \___   ___ | | /\ /(_) |_  #
#   | | | | | | | / /____ / /\/ _ \ / _ \| |/ //_/ | __| #
#   | |_| | |_| |/ /_____/ / | (_) | (_) | / __ \| | |_  #
#    \___/ \___//_/      \/   \___/ \___/|_\/  \/|_|\__| #
#                                                        #
#     [-] Developed & Coded by Bond Benz                 #
#                                                        #
##########################################################
"""

menu = """

[1] - Website Server Extractor
[2] - Simple Dorker
[3] - Password Generator
[4] - Wordlist Generator
[5] - About me
[6] - Exit


"""


def aboutme():
    print '''
##########################################################
#     ____  _____  _  _  ____  ____  ____  _  _  ____    #
#    (  _ \(  _  )( \( )(  _ \(  _ \( ___)( \( )(_   )   #
#    ) _ < )(_)(  )  (  )(_) )) _ < )__)  )  (  / /_     #
#   (____/(_____)(_)\_)(____/(____/(____)(_)\_)(____)    #
#                                                        #
#     E-mail : s0-z.x@hotmail.com                        #
#     Facebook : https://www.facebook.com/0x55547987     #
#     Team : 1337Day Algeria                             #
#                                                        #
#                                                        #
##########################################################

'''


def Dorker():
    print "[+] Rule N1 : Don't Put inurl: or intext: or something like that"
    print "[+] Rule N2 : Don't Use Space In The Dork or the script wont work"
    dork = raw_input('Dork : ')
    print "[~] Result : "
    page = 1
    sites = list()
    while page <= 150:

        url = "http://www.bing.com/search?q="+dork+"+node&go=Valider&qs=ds&form=QBRE&first=" + str(page)
        req = urllib2.Request(url)
        read = urllib2.urlopen(req).read()
        extract = re.findall('<div class="b_title"><h2><a href="(.*?)" h=', read)
        page += 1

        for url in extract:
            split = urlparse(url)
            site = split.netloc
            if site not in sites:
                print site
                sites.append(site)


def ipextract():
    ip = raw_input('Server IP : ')
    print "[~] Result : "
    page = 1
    sites = list()
    while page <= 150:

        url = "http://www.bing.com/search?q=ip%3A"+ip+"+node&go=Valider&qs=ds&form=QBRE&first=" + str(page)
        req = urllib2.Request(url)
        read = urllib2.urlopen(req).read()
        extract = re.findall('<div class="b_title"><h2><a href="(.*?)" h=', read)
        page += 1

        for url in extract:
            split = urlparse(url)
            site = split.netloc
            if site not in sites:
                print site
                sites.append(site)


def wordlist():
    chars = raw_input('Name to make the wordlist : ')
    n = 5

    for xs in itertools.product(chars, repeat=n):
        print ''.join(xs)

    exit()


def generator():
    print '''

   [1] - Password Length 6 Digits
   [2] - Password Length 8 Digits
   [3] - Password Length 12 Digits


        '''
    chs = int(raw_input("Choose Password Type [1-3]: "))

    if chs == 1:
        length = 6
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        print "[~] Password Successfully Generated : "
        print ''.join(random.choice(chars) for i in range(length))
        exit()
    if chs == 2:
        length = 8
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        print "[~] Password Successfully Generated : "
        print ''.join(random.choice(chars) for i in range(length))
        exit()
    if chs == 3:
        length = 12
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        random.seed = (os.urandom(1024))
        print "[~] Password Successfully Generated : "
        print ''.join(random.choice(chars) for i in range(length))
        exit()
    if chs < 1:
        print "[+] Please enter the right option"
        exit()
    if chs > 3:
        print "[+] Please enter the right option"
        exit()


def main():
    print logo
    print menu

    while True:
        choose = raw_input("[~] Choose an Option [1-6] : ")

        if not (int(choose) in range(1, 7)):
            print "Please Choose the Right Option"
            continue

        if choose == "1":
            ipextract()
        elif choose == "2":
            Dorker()
        elif choose == "3":
            generator()
        elif choose == "4":
            wordlist()
        elif choose == "5":
            aboutme()
        elif choose == "6":
            exit()

        con = raw_input('Continue [Y/n] -> ')
        if len(con) == 0 or con[0].upper() == 'Y':
            main()
        elif con[0].upper() == 'N':
            exit()
        else:
            pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\n\nPeace out! ;)\n  "
